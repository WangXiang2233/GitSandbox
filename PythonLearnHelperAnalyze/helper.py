import xlrd

# #########################################

masterFileName = "C:/Users/xi.wu/Documents/GitSandbox/PythonLearningHelperAnalyze/master_screen_list.txt"
resultFileName = "C:/Users/xi.wu/Documents/GitSandbox/PythonLearningHelperAnalyze/helper_list.csv"
logFileName = "C:/Users/xi.wu/Documents/GitSandbox/PythonLearningHelperAnalyze/log.csv"

# #########################################

def getLv5Id(fileName):
    fileNameSplit = fileName.split("_")
    countOfSeperator = len(fileNameSplit)
    return fileNameSplit[countOfSeperator - 2]

def getLv5Name(fileName):
    fileNameSplit = fileName.split("_")
    countOfSeperator = len(fileNameSplit)
    lv5NameWithDot = fileNameSplit[countOfSeperator - 1];
    lv5NameWithDotSplit = lv5NameWithDot.split(".")
    return lv5NameWithDotSplit[0]

# #########################################

resultFile = open(resultFileName, mode='w')
resultFile.write('lv5id, lv5name, line#, area, ssid, itemname, type\n')

logFile = open(logFileName, mode='w')
logFile.write('lv5id, lv5name, with helper\n')

with open(masterFileName) as f:
    masterFileNames = f.read().splitlines()

for masterFileName in masterFileNames:

    print(masterFileName)

    lv5Id = getLv5Id(masterFileName)
    lv5Name = getLv5Name(masterFileName)
    containsHelperSheet = False

    book = xlrd.open_workbook(masterFileName)
    sheetNames = book.sheet_names()
    for sheetName in sheetNames:
        if sheetName.startswith('ItemDefinition'):
            sheet = book.sheet_by_name(sheetName)

            isInHelperArea = False
            for row in range(0, sheet.nrows):
                area = sheet.cell(row, 1).value

                if (area == 'Body(Helper)'):
                    isInHelperArea = True
                    containsHelperSheet = True

                if (isInHelperArea == False):
                    continue

                if (area == 'e'):
                    break

                if (isInHelperArea == True):
                    screenItemId = sheet.cell(row, 2).value
                    itemName = sheet.cell(row, 4).value
                    controllerType = sheet.cell(row, 6).value

                    resultStr = ''
                    resultStr = resultStr + lv5Id + ","
                    resultStr = resultStr + lv5Name + ","
                    resultStr = resultStr + str(row) + ","
                    resultStr = resultStr + area + ","
                    resultStr = resultStr + screenItemId + ","
                    resultStr = resultStr + itemName + ","
                    resultStr = resultStr + controllerType
                    resultStr = resultStr + "\n"
                    resultFile.write(resultStr)

    logStr = ''
    logStr = logStr + lv5Id + ","
    logStr = logStr + lv5Name + ","
    logStr = logStr + str(containsHelperSheet)
    logStr = logStr + "\n"
    logFile.write(logStr)
 
resultFile.close
logFile.close
