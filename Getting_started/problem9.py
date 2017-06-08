# predict output
x=1
def f():
	x=2
	return x

print x    # output :1
print f()  # output: 2
print x    # output: 1
