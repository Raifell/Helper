import openpyexcel

wb = openpyexcel.load_workbook(path)
ws = wb.active

li = []

for i in range(0, ws.max_row):
    l = []
    for col in ws.iter_cols(0, ws.max_column):
        l.append(col[i].value)
    li.append(l)

wb.close()

print(*li, sep="\n")
