#problem13 function to comapre words without checking case 
def istrcmp(arg1,arg2):
	if arg1.upper() == arg2.upper():
		return True
if __name__=='__main__':
	print istrcmp('python','Python')
	print istrcmp('a','b')
	print istrcmp('LaTex','Latex')
