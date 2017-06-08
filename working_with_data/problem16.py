# anand python problem 2:16
# implement a function that sort list of file name based in their extension

def extsort(lists):
	print lists
	a=sorted(lists,cmp=lambda x,y: cmp(x.split('.')[1],y.split('.')[1]))
	return a
def myst(lists):
	res=[]
	for i in range(len(lists)):
		lists[i]=lists[i].split('.')
	h=lambda f:f[1]
	lists.sort(key=h)
	for i in lists:
		res.append('.'.join(i)) 	
	
	return res
if __name__ == '__main__':
	a=extsort(['a.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt', 'x.c'])
	print a
	b= myst(['a.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt', 'x.c'])
	print b
