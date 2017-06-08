# anand python problem 8 5:8
#Write a function peep, that takes an iterator as argument and returns the first element and an equivalant iterator.
def peep(iterator):
	res=list(iterator)
	return res[0],res
if  __name__ == '__main__':
	iter1=iter(range(5))
	print peep(iter1)
