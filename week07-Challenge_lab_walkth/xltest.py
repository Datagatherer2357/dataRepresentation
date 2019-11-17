# For testing to get rid of errors

import xlwt

workbook = xlwt.Workbook('hello.xlsx')
worksheet = workbook.add_worksheet()

worksheet.write('A1', 'Hello world')

workbook.close()