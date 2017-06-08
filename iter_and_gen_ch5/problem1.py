#anand python problem 1 5:1
#Write an iterator class reverse_iter, that takes a list and iterates it from the reverse direction. ::
#
class reverse_iter:
	def __init__(self,lists):
		self.lists=lists
		self.size=len(lists)
	def __iter__(self):
		return self
	def next(self):
		
		if self.size>0:
			self.size-=1
			return self.lists[self.size]
		else:
			raise StopIteration()

a=reverse_iter([1,2,3,4,5])
print a.next()
print a.next()
				
			
		
		
		
