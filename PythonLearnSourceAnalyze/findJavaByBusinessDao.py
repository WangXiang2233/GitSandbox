# ## import
import os
import logging
import re
import sys

# ## const
CHANGED_TBL_NAME = sys.argv[1]
ROOT_DIR = 'C:/NeaProject/projects.temp/'
SUBSTEM_BATCH_DIR = ROOT_DIR + 'Gaf{}App/Gaf{}Batch/src/main/java/'
SUBSTEM_COMMONLIB_DIR = ROOT_DIR + 'Gaf{}App/Gaf{}CommonLib/src/main/java/'
SUBSTEM_WEB_DIR = ROOT_DIR + 'Gaf{}App/Gaf{}Web/src/main/java/'
BIZCOMMONLIB_DIR = ROOT_DIR + 'GafBizCommonLib/GafBizCommonLib/src/main/java/'
HELPER_DIR = ROOT_DIR + 'GafHelperApp/GafHelperWeb/src/main/java/'
SUBSYSTEM_LIST_FILE = ROOT_DIR + 'XFind/subsystem_list.txt'
BUSINESS_DAO_LIST_FILE = ROOT_DIR + 'XFind/business_dao_list.txt'
RESULT_FILE = ROOT_DIR + 'XFind/java_by_business_dao.txt'
LOG_FILE = ROOT_DIR + 'XFind/find_java_by_business_dao.log'
LOG_FORMAT = '[%(asctime)s][%(levelname)s] %(message)s'

# ## class

# ## global variable

# ## sub functions 

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
        if path[-5:] == '.java':
            find = keywordInFile(path, keyword)
            if find:
                logging.debug('FIND! path={},keyword={}'.format(path, keyword))
                resultFile = open(RESULT_FILE, mode='a+')
                resultFile.write(CHANGED_TBL_NAME + ',' + keyword + ',' + pathToDaoName(path) + '\n')
                resultFile.close()

# ## main functions 
def main():

    logging.info('======== START ========')

#    if os.path.exists(RESULT_FILE):
#        os.remove(RESULT_FILE)

    with open(BUSINESS_DAO_LIST_FILE) as businessDaoListFile:
        for businessDao in businessDaoListFile:
            if businessDao.endswith('\n'):
                businessDao = businessDao[:-1]

            recursiveFileCheck(BIZCOMMONLIB_DIR, businessDao)
            recursiveFileCheck(HELPER_DIR, businessDao)
            
            with open(SUBSYSTEM_LIST_FILE) as subsystemListFile:
                for subsytem in subsystemListFile:
                    if subsytem.endswith('\n'):
                        subsytem = subsytem[:-1]
                        subsytem = subsytem.capitalize()

                        logging.info('check {} {}'.format(subsytem, businessDao))

                        recursiveFileCheck(SUBSTEM_BATCH_DIR.format(subsytem,subsytem), businessDao)
                        recursiveFileCheck(SUBSTEM_COMMONLIB_DIR.format(subsytem,subsytem), businessDao)
                        recursiveFileCheck(SUBSTEM_WEB_DIR.format(subsytem,subsytem), businessDao)

    logging.info('======== END ========')

# ## entrance 
if __name__ == "__main__":
    logging.basicConfig(filename=LOG_FILE, level=logging.DEBUG, format=LOG_FORMAT)
    main()

