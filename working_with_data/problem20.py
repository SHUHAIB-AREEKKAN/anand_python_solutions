# anand python problem 2:20
# implment simple grep ,to find a line which has the input word 

import sys

def grep(filename,fnd):
	outs=[]
	res=open(filename).readlines()
	for i in res:
		if fnd in i:
			print i
			outs.append(i)
	return outs
			



if __name__=='__main__':
	a=grep(sys.argv[1],sys.argv[2])
