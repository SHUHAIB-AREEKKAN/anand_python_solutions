# anand python chapter 2 :1
x=[0,1,[2]]
x[2][0]=3
print x 	# x=[0,1,[3]]
x[2].append(4) 
print x		# x=[0,1,[3,4]] #we are appending 4 to nested list 
x[2]=2
print x 	# x=[0,1,2]
