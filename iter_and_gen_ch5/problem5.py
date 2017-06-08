#anand python 5 5:5
# Write a function to compute the total number of lines of code in all python fi#les in the specified directory recursively.
import os
import sys
cnt=0
def get_path(direc):
	for i in os.listdir(direc):
		paths=os.path.join(direc,i)
		yield paths
def get_line(filename):
	return (line for line in open(filename))

def print_path(direc):
	global cnt
	for path in get_path(direc):
		if os.path.isfile(path):
			 if '.py' == os.path.splitext(path)[1].lower():
				for i in get_line(path):
					cnt+=1								
		else:
			print_path(path)
	return cnt

def main(direc):
	sec=print_path(direc)
	print 'No of  lines in all py files {} : {}'.format(direc,sec)

if __name__ == '__main__':
	main(sys.argv[1])
	
