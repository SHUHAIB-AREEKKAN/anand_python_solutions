# anand python problem 1 6:1
# Implement a function product to multiply 2 numbers recursively using + and - operators only.

def multiply(x,y):
	if x == 1 :
		return y
	elif y==1:
		return x
	elif x==0 or y==0:
		return 0
	else:
		return x+multiply(x,y-1)

if __name__ == '__main__':
	print multiply(8,4)
