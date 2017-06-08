#anand_python question 2:9
#cummulative multipication of list values

def cummulative_mul(lists):
	res=[]
	pre_sum=1
	for i in lists:
		pre_sum=pre_sum * i
		res.append(pre_sum)
	return res
if __name__=='__main__':
	a=cummulative_mul([1,2,3,4])
	print a	
