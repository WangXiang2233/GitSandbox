# ## import
import os
import logging
import re
import sys

# ## const
CHANGED_TBL_NAME = sys.argv[1]
ROOT_DIR = 'C:/NeaProject/projects.temp/'
SUBSTEM_DIR = ROOT_DIR + 'Gaf{}App/Gaf{}DaoLib/src/main/resources/'
SUBSYSTEM_LIST_FILE = ROOT_DIR + 'XFind/subsystem_list.txt'
RESULT_FILE = ROOT_DIR + 'XFind/table_dao_list.txt'
LOG_FILE = ROOT_DIR + 'XFind/find_table_dao.log'
LOG_FORMAT = '[%(asctime)s][%(levelname)s] %(message)s'

# ## class

# ## global variable

# ## sub functions 

def removeDuplicateLine(filename):
    result = []

    with open(filename) as f:
        for line in f:
            if line.endswith('\n'):
                line = line[:-1]
                
            if line not in result:
                result.append(line)

    with open(filename, 'w') as f:
        for line in result:
            f.write(line + '\n')

def left(s, amount):
    return s[:amount]

def pathToDaoName(path):
    dirname, basename = os.path.split(path)
    ridx = basename.rfind('.')
    return left(basename, ridx)

def tableToEntityName(tablename):
    result = ''

    wordList = tablename.split('_')
    for word in wordList:
        word = word.capitalize()
        result += word

    result += "Entity"
    return result

def keywordInFile(path, keyword):
    find = False
    with open(path, encoding='utf-8') as f:
        for line in f:
            match = re.search(keyword, line)
            if match:
                return True

    return find

def recursiveFileCheck(path, keyword):

    logging.debug('path={},keyword={}'.format(path, keyword))

    if os.path.isdir(path):
        # directoryだったら
        files = os.listdir(path)
        for file in files:
            recursiveFileCheck(path + '/' + file, keyword)
    else:
        # fileだったら
        if path[-4:] == '.xml':
            find = keywordInFile(path, keyword)
            if find:
                logging.debug('FIND! path={},keyword={}'.format(path, keyword))
                resultFile = open(RESULT_FILE, mode='a+')
                resultFile.write(pathToDaoName(path) + '\n')
                resultFile.close()

# ## main functions 
def main():

    logging.info('======== START ========')

    logging.info('keyword = {}'.format(CHANGED_TBL_NAME))

    if os.path.exists(RESULT_FILE):
        os.remove(RESULT_FILE)

    with open(SUBSYSTEM_LIST_FILE) as subsystemListFile:

        for line in subsystemListFile:
            if line.endswith('\n'):
                line = line[:-1]

            line = line.capitalize()
            logging.info('check sub system : {}'.format(line))

            path = SUBSTEM_DIR.format(line, line)
            recursiveFileCheck(path, CHANGED_TBL_NAME)
            recursiveFileCheck(path, tableToEntityName(CHANGED_TBL_NAME))

    removeDuplicateLine(RESULT_FILE)
    logging.info('======== END ========')

# ## entrance 
if __name__ == "__main__":
    logging.basicConfig(filename=LOG_FILE, level=logging.DEBUG, format=LOG_FORMAT)
    main()

