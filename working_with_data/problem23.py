#anand python problem 2: 23
#Write a program center_align.py to center align all lines in the given file.

import sys

def center_align(filename):
	f=open(filename).readlines()
	big_line=len(max(f))
	for line in f:
		p=(big_line-len(line)/2) #biggest lien l - current line l/2
		print ' '*p+line





if __name__=='__main__':
	center_align(sys.argv[1])
