#anand_python question 2:10
#find a uniques  in a list of values values

def unique_find(lists):
	x=lists[1:]
	res=[]
	for i in lists:
		if i not in x:
			res.append(i)
		x=x[1:]	
	return res
def simple_unique(lists):
	res=[]
	for i in lists:
		if i not in res:
			res.append(i)
	return res	 
		
		
		
	
	
if __name__=='__main__':
	a=unique_find([1,2,3,4,5,1,5,4,3])
	print a	
	b=simple_unique([1,2,3,4,5,1,5,4,3])
	print b
