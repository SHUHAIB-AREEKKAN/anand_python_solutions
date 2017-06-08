# anand python problem 2:25
# Python provides a built-in function map that applies a function to each element of a list. Provide an implementation for map using list comprehensions

def map_imp(f,lists):
	a=[f(i) for i  in lists ]
	print a

def square(x):
	return x*x



if __name__=='__main__':
	map_imp(square,range(5))
