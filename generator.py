# import xlsxwriter module
import sys
import xlsxwriter
from faker import Faker
from numerize import numerize
fake = Faker(['en_US'])

dataSize = int(sys.argv[1])
workbook = xlsxwriter.Workbook(f'woosender-{numerize.numerize(dataSize)}.xlsx')
worksheet = workbook.add_worksheet()
dataset = [[fake.first_name(), fake.last_name(), fake.company_email() , f'+1{fake.msisdn()[:-3]}', fake.company(), 'test'] for i in range(dataSize)]
 
# iterating through content list
row = 0
worksheet.write_row(row, 0, ["First Name", "Last Name", "Email", "Phone Number", "Company", "Tag"])
row+=1
for data in dataset :
    worksheet.write_row(row, 0, data)
    row+=1
     
workbook.close()