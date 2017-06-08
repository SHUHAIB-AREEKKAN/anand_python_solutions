#anand_python question 2:6
# reverse a list 
def reverse_list(lists):
	res=[]
	for i in range(len(lists)-1,-1,-1):
		res.append(lists[i])
	return res

ins=[1,2,3,4]
a=reverse_list(ins)
print a
	  	

