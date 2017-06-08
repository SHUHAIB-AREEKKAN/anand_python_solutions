import sys
# add two numbers from cmd argument
def sum_of_two():
	tot=int(sys.argv[1]) + int(sys.argv[2])
	return tot

if __name__=='__main__':
	if len(sys.argv) >2:
		a=sum_of_two()
		print a	
