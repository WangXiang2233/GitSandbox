# ## import
import xlrd
from datetime import datetime 

# ## const
HOME_DIR = 'C:/Users/xi.wu/Desktop/'

# ## class

# ## global variable
today = datetime.now().strftime("%Y%m%d")
inputBookFileName = HOME_DIR + 'release_note_tool.xlsx'
resultFileName = HOME_DIR + 'release_note_{}.txt'.format(today)

# ## sub functions 

def left(s, amount):
    return s[:amount]

def right(s, amount):
    return s[-amount:]

def mid(s, offset, amount):
    return s[offset:offset+amount]

def find2nd(s, substring):
   return s.find(substring, s.find(substring) + 1)

# ## main functions 
def main():
    print('>>> start >>>')

    functionIdList = list()
    webSubsystems = set()
    batchSubsystems = set()
    asteriaFunctionIds = set()

    # read input excel file 
    book = xlrd.open_workbook(inputBookFileName)

    # UnitApply sheet
    sheet = book.sheet_by_name('UnitApply')
    print(str(sheet.nrows) + " lines in UnitApply")
    for row in range(0, sheet.nrows):
        functionId = sheet.cell(row, 0).value
        functionIdList.append(functionId)

    # BugFix sheet
    sheet = book.sheet_by_name('BugFix')
    print(str(sheet.nrows) + " lines in BugFix")
    for row in range(0, sheet.nrows):
        bugTitle = str(sheet.cell(row, 0).value)
        functionIdIdx = find2nd(bugTitle, '[')
        functionIdIdxEnd = find2nd(bugTitle, ']')
        functionIdLen = functionIdIdxEnd - functionIdIdx - 1
        functionId = mid(bugTitle, functionIdIdx + 1, functionIdLen)
        functionIdList.append(functionId)

    # walkthrough all functionIds
    for functionId in functionIdList:
        if len(functionId) != 13:
            print('<warning> ' + " functionId : " + functionId)
        else:
            subSystem = left(functionId, 2).capitalize()
            functionType = mid(functionId, 2, 1).capitalize()

            if functionType == 'D': 
                # screen
                webSubsystems.add(subSystem)
            elif functionType == 'P': 
                # report
                webSubsystems.add(subSystem)
            elif functionType == 'B':
                # batch
                batchSubsystems.add(subSystem)
            elif functionType == 'I':
                # interface
                batchSubsystems.add(subSystem)
                asteriaFunctionIds.add(functionId)
            else:
                print('<warning> ' + " functionId : " + functionId)

    # output
    resultFile = open(resultFileName, mode='w')
    resultFile.write('<< ' + today + ' >>\n\n')

    allSubsystems = webSubsystems | batchSubsystems
    for subSystem in allSubsystems:
        s = subSystem
        if subSystem in webSubsystems:
            s += " Web "
        if subSystem in batchSubsystems:
            s += " batch "
     
        resultFile.write(s + '\n')

    if len(webSubsystems) > 0:
        resultFile.write('HelperWeb' + '\n')
    
    if len(batchSubsystems) > 0 or len(asteriaFunctionIds) > 0:
        resultFile.write('BatchScript' + '\n')

    if len(asteriaFunctionIds) > 0:
        resultFile.write('Asteria' + '\n')

    for asteriaFunctionId in asteriaFunctionIds:
        resultFile.write('\t' + asteriaFunctionId + '\n')

    resultFile.write('??? DB_DDL ??? please check !' + '\n')
    resultFile.write('??? DB_DML ??? please check !' + '\n')

    # finalize
    resultFile.close
    print('<<< end <<<')

# ## entrance 
if __name__ == "__main__":
    main()

