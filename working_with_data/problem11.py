#anand_python problem 2:11
# find duplicate elements in a list
def find_dups(lists):
	dups=[]
	for i in range(len(lists)):
		for j in range(i+1,len(lists)):
			if lists[i] == lists[j]:
				dups.append(i)
	return dups


if __name__ == '__main__':
	a=find_dups([0,1,2,3,1,5,5,0])  
	print a
