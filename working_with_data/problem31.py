#anand python problem 2:31
#Generalize the above(30 problem) implementation of csv parser to support any delimiter and comments.

def parse_csv(filename,d,c):
	csv_data=[]
	f=open("parsed_csv.csv","w+")
	tmp=open(filename)
	for i in tmp.readlines():
		if i.startswith(c):
			print 
		else:
			csv_data.append(i)	
		
	for k in csv_data:
		f.write(k.replace(d,','))
def another_parser(filename,delimeter,comment):
	a=[x[:-1].replace(delimeter,',') for x in open(filename).readlines() if x[0]!=comment  ]

	print a


	
if __name__ =='__main__':

	parse_csv('he.csv','!','#')
	another_parser('he.csv','!','#')



