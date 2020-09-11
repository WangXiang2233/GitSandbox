import xlrd
import datetime

# #########################################

class GafTask:
    redmine_id = 0
    sub_team = ""
    func_id = ""
    func_name = ""
    task_no = ""
    task_name = ""
    pic_member = ""
    pic_on = ""
    status = ""
    planned_effort = 0.0
    plan_start = datetime.datetime.strptime('19000101', '%Y%m%d')
    actul_start = datetime.datetime.strptime('19000101', '%Y%m%d')
    plan_end = datetime.datetime.strptime('19000101', '%Y%m%d')
    actul_end = datetime.datetime.strptime('19000101', '%Y%m%d')

class GafFunction:
    tasks = []
    sub_team = ""
    func_id = ""
    func_name = ""

    def __init__(self):
        tasks = []

# #########################################

def to_datetime(cell):
    return xlrd.xldate_as_datetime(cell.value, book.datemode)

# #########################################

resultFileName = "C:/Users/xi.wu/Documents/GitSandbox/PythonLearningIFRemarkAnalyze/IFlistRemarks.csv"

# #########################################

book = xlrd.open_workbook('C:/Users/xi.wu/Documents/GitSandbox/PythonLearningScheduleAnalyze/schedule.xlsx')
sheet = book.sheet_by_name('スケジュール')

functions = []
for row in range(5, sheet.nrows):
    if (sheet.cell(row, 0).value == 'e'):
        break
    elif ((row - 5) % 18 == 0):
        function = GafFunction()
        function.sub_team = sheet.cell(row, 2).value
        function.func_id = sheet.cell(row, 3).value
        function.func_name = sheet.cell(row, 4).value
        function.tasks = []
        functions.append(function)
    else:
        task = GafTask()
        task.redmine_id = int(sheet.cell(row, 0).value)
        task.sub_team = sheet.cell(row, 2).value
        task.func_id = sheet.cell(row, 3).value
        task.func_name = sheet.cell(row, 4).value
        task.task_no = sheet.cell(row, 5).value
        task.task_name = sheet.cell(row, 7).value
        task.pic_member = sheet.cell(row, 8).value
        task.pic_on = sheet.cell(row, 9).value
        task.status = sheet.cell(row, 11).value
        task.planned_effort = float(sheet.cell(row, 12).value)
        if (sheet.cell(row, 13).value != ''):
            task.plan_start = to_datetime(sheet.cell(row, 13))
        if (sheet.cell(row, 14).value != ''):
            task.plan_end = to_datetime(sheet.cell(row, 14))
        if (sheet.cell(row, 15).value != ''):
            task.actul_start = to_datetime(sheet.cell(row, 15))
        if (sheet.cell(row, 16).value != ''):
            task.actul_end = to_datetime(sheet.cell(row, 16))
        function.tasks.append(task)

for function in functions:
    status = function.tasks[7].status
    end_date = function.tasks[7].actul_end
    accept_status = function.tasks[8].status
    accept_end_date = function.tasks[8].actul_end
    if status == '完了/Finish' and accept_status != '完了/Finish':
        gap = (datetime.datetime.now() - end_date).days

        print(function.func_id, function.func_name,'delay:', gap, 'days')

