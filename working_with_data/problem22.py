# anand python problem 2: 22
#The above wrap program is not so nice because it is breaking the line at middle of any word. Can you write a new program wordwrap.py that works like wrap.py, but breaks the line only at the word boundaries?

import sys

def wordwrap(filename,size):
	tot=0
	#fes=open(frome.txt)
	stradd=''
	res=[]
	for i in open(filename).readlines():
		tot=0		# readlines : every line on by one to i (by mechanisam as list)
		if len(i)>size:
			print						# if length of line bigger than size 
			for k in i.split():
				tot+=len(k)
				if tot<size:					# we split in to words
					print k,
				else:
					print
					print k,
						
			res.append(stradd)		
		else:
			print i			


if __name__ == '__main__':
	print wordwrap(sys.argv[1],int(sys.argv[2]))
