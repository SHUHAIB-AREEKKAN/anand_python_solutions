# anand python problem 7
# Write a program split.py, that takes an integer n and a filename as command line arguments and splits the file into multiple small files with each h#aving n lines.

import os


def read_line(filename):
	return(line for line in open(filename))

def split(filename,limit=2):
	count=0
	file_prefix=1
	f=open('split_0'+os.path.splitext(filename)[1],'w')
	for line in read_line(filename):
		if count == limit:
			f.close()
			f=open('split_'+str(file_prefix)+os.path.splitext(filename)[1],'w')
			count=0
			file_prefix+=1
		f.write(line)
		count+=1
	f.close()
			





if __name__ == '__main__':

	split('two.txt',3)		
