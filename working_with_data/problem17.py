#anand python problem 2:17
# read a text file in reverse order
import sys
def reverse_print(filename):
	f=open(filename)
	res=f.readlines()
	for i in range(len(res)-1,-1,-1):
		print res[i]



if __name__=='__main__':
	reverse_print(sys.argv[1])

