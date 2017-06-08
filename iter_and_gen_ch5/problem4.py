# anand python problem 4 5:4
# Write a function to compute the number of python files (.py extension) in a specified directory recursively.
#


import os
import sys
cnt=0
def get_path(direc):
	for i in os.listdir(direc):
		paths=os.path.join(direc,i)
		yield paths
def print_path(direc):
	global cnt
	for path in get_path(direc):
		if os.path.isfile(path):
			 if '.py' == os.path.splitext(path)[1].lower():
				cnt+=1								
		else:
			print_path(path)
	return cnt

def main(direc):
	sec=print_path(direc)
	print 'No of file in the directory {} : {}'.format(direc,sec)

if __name__ == '__main__':
	main(sys.argv[1])
	
