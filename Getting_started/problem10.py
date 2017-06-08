# predict output

x = 1
def f():
        y = x # next stmt x=2 will cause error bcz global var x
        x = 2 
        return x + y
print x
print f()
print x
 # output is error 
