f=lambda x: x.lower()
def simple_unique(lists,keys):
	res=[]
	for i in lists:
		if f(i) not in res:
			res.append(i)
	return res
a=simple_unique(['aa','AA','b','D','d','c','Aa','B'],f)
print a
