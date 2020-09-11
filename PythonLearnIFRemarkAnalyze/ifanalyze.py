import xlrd

# #########################################

ifListFileName = "C:/Users/xi.wu/Documents/GitSandbox/PythonLearningIFRemarkAnalyze/IFlist.txt"
resultFileName = "C:/Users/xi.wu/Documents/GitSandbox/PythonLearningIFRemarkAnalyze/IFlistRemarks.csv"

# #########################################

resultFile = open(resultFileName, mode='w')

with open(ifListFileName) as f:
    ifFileNames = f.read().splitlines()

for ifFileName in ifFileNames:
    print(ifFileName)

    book = xlrd.open_workbook(ifFileName)
    sheetNames = book.sheet_names();

    for sheetName in sheetNames:
        if sheetName.startswith('Layout'):
            sheet = book.sheet_by_name(sheetName)

            for row in range(13, sheet.nrows):
                no = sheet.cell(row, 0).value
                itemName = sheet.cell(row, 2).value
                remarks = sheet.cell(row, 12).value
                if (no == 'e'):
                    break
                elif (no == ''):
                    continue
                elif (no == 'No' or no == 'No.' or no == ' Lv'):
                    continue
                elif (remarks == ''):
                    continue
                else:
                    s = ifFileName
                    s += ',' + sheetName
                    s += ',' + str(no)
                    s += ',' + itemName
                    s += ',' + remarks.replace('\n',' ')
                    s += ',' + '\n' 
                    resultFile.write(s)

resultFile.close
