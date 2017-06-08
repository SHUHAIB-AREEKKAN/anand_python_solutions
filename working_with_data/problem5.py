#anand_python question 2:5
#factorial implmentation

def fact_of_no(no):
	fact=1
	for i in range(1,no+1):
		fact=fact*i
	return fact
if __name__=='__main__':
	a=fact_of_no(4)
	print a
