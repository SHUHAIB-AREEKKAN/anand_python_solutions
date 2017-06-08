# anand python problem 2:37
#Write a function valuesort to sort values of a dictionary based on the key.
def valuesort(dic):
	return [dic[x] for x in sorted(dic.keys())]




if __name__ == '__main__':

	print valuesort({'x': 1, 'y': 2, 'a': 3})

	
