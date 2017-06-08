#anand python problem 2:29
#Write a function array to create an 2-dimensional array. The function should take both dimensions as arguments. Value of each element can be initialized to None:
#

def array_imp(row,col):
	res=[[None]*col for i in range(row) ]
	return res




if __name__=='__main__':
	outs=array_imp(2,3)
	print outs
