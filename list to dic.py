# from operator import length_hint
#
# import openpyxl
#
# book = openpyxl.load_workbook("C:\\Users\\helpe\\Desktop\\test.xlsx")
# sheet = book.active
# cell = sheet.cell(row=1, column=1).value
# cell2= sheet.cell(row=2, column=1).value
#
# l1= ["username", "password"]
# l2= [cell, cell2]
#
# dt={}
#
# for i in range(2):
#     dt[i]=l2[i-1]
#
# print(dt)

arr = [1, 0, 0, 1, 1, 0, 1, 0]

# Pointer to place next 0
index = 0

# Move all 0s to the front by swapping
for i in range(len(arr)):
    if arr[i] == 0:
        arr[i], arr[index] = arr[index], arr[i]
        index += 1

print(arr)