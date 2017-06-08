#anad python 2:35
#Write a program to count frequency of characters in a given file. Can you use character frequency to tell whether the given file is a Python program file, C program file or a text file?

import sys

def read_char(filename):
	return open(filename).read()
def char_frequency(chars):
	frequency={}
	for c in chars:
		frequency[c]=frequency.get(c,0) + 1
	return frequency

def sort_frequency(filename):
	sec=char_frequency(read_char(filename))
	
	sec2=[[x,k] for x,k in sec.items()]
	sec3=sorted(sec2,key=lambda x: x[1],reverse=True)
	for k in sec3:
		print k

def filetype(filename):
	a=filename.split('.')
	print 'type of file : ',a[-1]


if __name__ == '__main__':
	filename=sys.argv[1]
	sort_frequency(filename)
	filetype(filename)
	
	

