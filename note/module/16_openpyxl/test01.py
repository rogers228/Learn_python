import openpyxl

def test1():
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet_title = sheet.title
    print("active sheet title: ", sheet_title)

if __name__ == '__main__':
    test1()