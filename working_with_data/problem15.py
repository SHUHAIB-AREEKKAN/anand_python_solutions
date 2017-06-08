#anand python problem 2:15
#re implement the unique in a list with sets

def unique_in_list(lists):
	res=set(lists)
	return res


if __name__=='__main__':

	a=unique_in_list([1,2,3,1,3])
	print a

