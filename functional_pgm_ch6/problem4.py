# anand python problem 4 6:4
# Write a function treemap to map a function over nested list.


def treemap(func,lists,result=None):
	if result is None:
		result=[]
	for i in lists:
		if  isinstance(i,list):
			result.append(treemap(func,i))
		else:
			result.append(func(i))
	return result	
	


if __name__ == '__main__':
	print treemap(lambda x: x*x, [1, 2, [3, 4,[5]]])
	# output:[1, 4, [9, 16, [25]]
