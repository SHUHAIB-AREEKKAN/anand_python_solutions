#anand python problem 13 3:13
#Write a program csv2xls.py that reads a csv file and exports it as Excel file. The prigram should take two arguments. The name of the csv file to read as first argument and the name of the Excel file to write as the second argument.
#

import tablib
data=tablib.Dataset()
def csv_to_xls(csv_name,xls_name):
	sec=open(csv_name).readlines()
	csv_parse=[]
	for i in sec:
		csv_parse.append(i[:-2].split(','))
	#print csv_parse
	for k in csv_parse:
		data.append(k)
	with open(xls_name,'wb') as f:
		f.write(data.xls)

		





if __name__ == '__main__':
	csv_to_xls('test.csv','target.xls')

