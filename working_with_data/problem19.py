#anand python problem 2:19
#implement unix commands head and tail

import sys

def head(filename):
	res=open(filename).readlines()
	for i in range(10):
		print res[i]
def tail(filename):
	res=open(filename).readlines()
	for i in range(len(res)-1,len(res)-11,-1):
		print res[i]





if __name__=='__main__':
	print head(sys.argv[1])
	print('Tail ******* start')
	print tail(sys.argv[1])
