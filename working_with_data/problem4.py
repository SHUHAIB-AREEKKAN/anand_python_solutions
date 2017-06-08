# anand_python question  2:4
#implementation list product
 
def sum_imp(lists):
	total=1
	for i in lists:
		if type(i) is int:
			total*=i
		else:
			try:
				total=int(i)*total
			except ValueError:
				print 'Not accepted'
	return total

if __name__=='__main__':
	
	a=sum_imp([5,5,5])
	print a
