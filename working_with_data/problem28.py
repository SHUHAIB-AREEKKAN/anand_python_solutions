# anand python problem 2:28
# implement enumerate that takes a list and return tuple with respect index

def enum_imp(lists):
	res=[(x,lists[x]) for x in range(len(lists))]
	return res




if __name__== '__main__':

	a=enum_imp(["a","b","c"])
	print a

