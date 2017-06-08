# anand python problem5  6:5
# Write a function tree_reverse to reverse elements of a nested-list recursively

def tree_reverse(lists,result=None,times=1):
	#print 'input ',lists

	lists.reverse()
	#print 'ins reveresed:',lists
	for i in lists:
		if isinstance(i,list):
			tree_reverse(i)
	#print lists		
	return lists

if __name__ == '__main__':

	print tree_reverse([[1, 2], [3, [4, 5]], 6])	
