

ass=[(1, 1, 2), (1, 2, 3), (1, 3, 4), (2, 1, 3), (2, 2, 4), (3, 1, 4),(2,3,5),(3,2,5)]
res=[]
emp=[]

def checks(a):
	for i in range(len(a)):
		for k in range(i+1,len(a)):
			if (a[i][0]==a[k][0] and a[i][1]==a[k][1]) or (a[i][0]==a[k][1] and a[i][1]==a[k][1]):
				res.append(a.index(a[k]))
	for ks in a:
		if a.index(ks) in res:
			print
		else:
			emp.append(ks)
	return emp
a=checks(ass)
print(a)


		
