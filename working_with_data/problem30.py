#anand python 2 : 30
#anand python problem 2:30
#implement simple function csv_parser

def parse_csv(filename):
        sec=[]
	res=open(filename).readlines()
	for r in res:
		sec.append(r.split())
	
	print sec



if __name__ == '__main__':
	parse_csv('he.csv')



