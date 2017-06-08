#anand python problem 3:2
#Write a program extcount.py to count number of files for each extension in the given directory. The program should take a directory name as argument and print count and extension for each available file extension.



import os
import sys

def count_extension(paths):
	ext_count={}
	for i in os.listdir(paths):
		name,ext=os.path.splitext(i)
		if ext:
			ext_count[ext]=ext_count.get(ext,0) + 1
	return ext_count	



if __name__ == '__main__':
	print count_extension(sys.argv[1])
