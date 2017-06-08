#anand python 9 problem 5:9
# The built-in function enumerate takes an iteratable and returns an iterator over pairs (index, value) for each value in the source.
#

import itertools
def my_enumerate(lists):
	return (itertools.izip(range(len(lists)),lists))
		

if __name__ == '__main__':
	sec=my_enumerate(['a','b','c'])	
	for a,b  in sec:
		print (a,b)
