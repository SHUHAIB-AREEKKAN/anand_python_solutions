#anand_python  problem 2:7
#min and max implementaion


def min_of_list(lists):
	mins=lists[0]
	for i in lists:
		if i<mins:
			mins=i
	return mins	
				

def max_of_list(lists):
	maxs=lists[0]
	for i in lists:
		if i>maxs:
			maxs=i
	return maxs	
				





if __name__=='__main__':
	a=min_of_list([5,6,1,5,0,3,2,1,8])
	print a
	b=max_of_list([5,6,1,5,0,3,2,1,8])
	print b

