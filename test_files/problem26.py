#anand python problem 2:26
#Python provides a built-in function filter(f, a) that returns items of the list a for which f(item) returns true. Provide an implementation for filter using list comprehensions.

def even(x): 
	return x % 2 == 0

def filter_imp(f,lists):
	a=[x for x in lists if f(x)]
	return a

if __name__=='__main__':
	print filter_imp(even,range(10))
