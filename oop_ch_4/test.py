class krange:
	def __init__(self,limit,dif=1):
		self.i=0
		self.limit=limit
		self.dif=dif
		
	def __iter__(self):
		return self
	def next(self):
		if self.i<self.limit:
			i=self.i
			self.i+=self.dif
			return i
		else:
			raise StopIteration()
 
x=krange(10,2)
print x.next()
print x.next()
print x.next()
print x.next()
print x.next()
print sum(krange(5))
print list(krange(5,2))

