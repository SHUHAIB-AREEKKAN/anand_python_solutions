def fast_exp(x,n):
	if n==0:
		return 1
	elif n%2==0:
		return fast_exp(x*x,n/2)
	else:
		return x * fast_exp(x,n-1)

fast_exp(2,10)
