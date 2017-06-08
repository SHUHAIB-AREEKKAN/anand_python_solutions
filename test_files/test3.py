import sys
def parse_csv(filename,d,c):
	a=[x[:-1].split(d) for x in open(filename,'r').readlines() if x[0]!=c]
	print a
filename='he.csv'
delim='!'
comment='#'
parse_csv(filename,delim,comment)
