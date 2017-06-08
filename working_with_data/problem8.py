#anand_python question 2:8
#cummulative addition of list values

def cummulative_add(lists):
	res=[]
	pre_sum=0
	for i in lists:
		pre_sum=pre_sum + i
		res.append(pre_sum)
	return res
if __name__=='__main__':
	a=cummulative_add([1,2,3,4])
	print a	
