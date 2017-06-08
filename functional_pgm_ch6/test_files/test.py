def exp(x,n,i=0):
	i+=1
	print ' x : {} and n : {}'.format(x,n)
	if n==0:
		return 1
	else:
		z=x * exp(x,n-1,i)
		print
		print' no : {} and result: {}'.format(i,z)
		print
		return x * exp(x,n-1,i)
exp(2,4)
