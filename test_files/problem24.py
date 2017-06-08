#anand python problem 2:24
#Provide an implementation for zip function using list comprehensions.


def zip_imp(a,b):

	h=[ (x,b[a.index(x)]) for x in a  ]
	return h


if __name__ == '__main__':
	res=zip_imp([1,2,3],['a','b','c'])
	print res
