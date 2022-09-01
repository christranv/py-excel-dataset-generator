# import xlsxwriter module
import sys
import xlsxwriter
from faker import Faker
from numerize import numerize
fake = Faker(['en_US'])

dataSize = int(sys.argv[1])
workbook = xlsxwriter.Workbook(f'dataset-{numerize.numerize(dataSize)}.xlsx')
worksheet = workbook.add_worksheet()
# iterating through content list
row = 0
worksheet.write_row(row, 0, ["First Name", "Last Name", "Email", "Phone Number", "Company", "Tag"])
row+=1
for data in dataset :
    worksheet.write_row(row, 0, data)
    row+=1
     
workbook.close()
