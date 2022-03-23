import openpyxl

book = openpyxl.Workbook()
sheet = book.active

sheet ["A1"] = "hello"
sheet ["B1"] ="world"

sheet.title = "titlu nou"
book.save("my.xls")

