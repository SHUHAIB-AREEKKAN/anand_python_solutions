#anand python problem 2:12
#implement groups from a list

def group_of_list(lists,size):
	res=[]
	st=0
	for i in range(size,len(lists),size):
		res.append(lists[st:i])
		#print(i)
		st=i
	if st!=len(lists):
		#print(st,len(lists),lists[st:])
		res.append(lists[st:])
		
	return res




if __name__=='__main__':
	a=group_of_list([1, 2, 3, 4, 5, 6, 7, 8, 9], 4)
	print a
	b=group_of_list([1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13], 3)
	print b
