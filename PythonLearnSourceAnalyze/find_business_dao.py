# ## import
import os
import logging
import re
import sys

# ## const

SOURCE_DIR = 'C:/NeaProject/projects.temp/'
BIZCOMMONLIB_DIR = SOURCE_DIR + 'GafBizCommonLib/GafBizCommonLib/src/main/resources/'

HOME_DIR = 'C:/Users/xi.wu/Documents/GitSandbox/PythonLearnSourceAnalyze/'
TABLE_LIST_FILE = HOME_DIR + 'in/table_list.txt'
TABLE_BUSINESS_DAO_FILE = HOME_DIR + 'out/table_business_dao.csv'
LOG_FILE = HOME_DIR + 'log/find_business_dao.log'
LOG_FORMAT = '[%(asctime)s][%(lineno)s] %(message)s'

# ## class

# ## global variable

# ## sub functions 

def makeCsvString(*args):
    result = ''
    for arg in args:
        result += arg
        result += ','

    if result.endswith(',') : result = result[:-1]
    return result

def removeCrLfFromLine(line):
    line = line.replace('\n', '')
    line = line.replace('\r', '')
    return line

def left(s, amount):
    return s[:amount]

def tableNameToEntityName(tablename):
    entityName = ''
    wordList = tablename.split('_')
    for word in wordList:
        word = word.capitalize()
        entityName += word
    entityName += "Entity"
    return entityName

def daoClassNameFromPath(path):
    dirname, basename = os.path.split(path)
    ridx = basename.rfind('.')
    return left(basename, ridx)

def keywordListInFile(path, table, entity):
    with open(path, encoding='utf-8') as f:
        contents = f.read()

    match = re.search(table, contents)
    if match: return True;

    match = re.search(entity, contents)
    if match: return True;

    return False

def recursiveFileCheck(table, entity, path, resultFileName):

    logging.debug('table={},entity={},path={}'.format(table, entity, path))

    if os.path.isdir(path):
        # directoryだったら
        files = os.listdir(path)
        for file in files:
            recursiveFileCheck(table, entity, path + '/' + file, resultFileName)
    else:
        # fileだったら
        if path[-4:] == '.xml':
            find = keywordListInFile(path, table, entity)
            if find:
                logging.info('FIND! keyword={},entity={},path={}'.format(path, table, entity))
                daoClassName = daoClassNameFromPath(path)
                csvstring = makeCsvString(table, daoClassName, path)

                resultFile = open(resultFileName, mode='a+')
                resultFile.write(csvstring + '\n')
                resultFile.close()

# ## main functions 
def main():

    logging.info('======== START ========')

    if os.path.exists(TABLE_BUSINESS_DAO_FILE):
        os.remove(TABLE_BUSINESS_DAO_FILE)

    with open(TABLE_LIST_FILE) as tableListFie:
        for tableName in tableListFie:
            tableName = removeCrLfFromLine(tableName)
            entityName = tableNameToEntityName(tableName)

            logging.info('tableName = {}'.format(tableName))
            recursiveFileCheck(tableName, entityName, BIZCOMMONLIB_DIR, TABLE_BUSINESS_DAO_FILE)

    logging.info('======== END ========')

# ## entrance 
if __name__ == "__main__":
    logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format=LOG_FORMAT)
    main()
