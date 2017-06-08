# anand python problem 10 5:10
# implement a function izip that works like itertools.izip.


def izip(list1,list2):
	i=0
	while i<len(list1):
		yield list1[i],list2[i]
		i=i+1
if __name__ == '__main__':
	for a,b in izip(['a','b'],[1,2]):
 		print a,b
