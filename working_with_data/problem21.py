#anand python problem 2:21
#  Write a program wrap.py that takes filename and width as aruguments and wraps the lines longer than width
import sys
def wrap(filename,size):
	for i in open(filename).readlines():

		if len(i)>size:
			print i[:size] 
			print i[size:len(i)]
		else:
			print i	
	
	#return res




if  __name__=='__main__':
	
	print wrap(sys.argv[1],int(sys.argv[2]))

