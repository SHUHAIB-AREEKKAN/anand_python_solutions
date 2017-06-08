#anand python problem 2:38
#Write a function invertdict to interchange keys and values in a dictionary. For simplicity, assume that all values are unique.

def invertdict(dic):
	sec={}
	for k,v in dic.items():
		sec[v]=k
	return sec





if __name__ == '__main__':
	print invertdict({'x': 1, 'y': 2, 'z': 3})
