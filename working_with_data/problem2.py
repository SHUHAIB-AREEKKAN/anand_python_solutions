# anand_python question  2:2
#implementation list sum
 
def sum_imp(lists):
	total=0
	for i in lists:
		if type(i) is int:
			total+=i
		else:
			try:
				total=int(i)+total
			except ValueError:
				print 'Not accepted'
	return total

if __name__=='__main__':
	
	a=sum_imp([1,2,3])
	print a
