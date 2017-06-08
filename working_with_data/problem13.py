#anand python problem 2:13
#sort a list based length of element
def lensort(lists):
	a=sorted(lists,key=len)
	return a



if __name__=='__main__':
	a=lensort(['python', 'perl', 'java', 'c', 'haskell', 'ruby'])
	print a
