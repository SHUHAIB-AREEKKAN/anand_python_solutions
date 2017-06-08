#anand python problem 2:18
#print each line in reverse order

import sys

def reverse_line(filename):
	j=''
	f=open(filename)
	outs=[]
	res=f.readlines()
	for i in res:
		print(i[::-1])




if __name__=='__main__':
	print reverse_line(sys.argv[1])
