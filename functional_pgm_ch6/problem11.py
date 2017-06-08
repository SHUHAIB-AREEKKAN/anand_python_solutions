# anand python problem 11 6:11
# Write a function vectorize which takes a function f and return a new function, which takes a list as argument and calls f for every element and returns the result as a list.
#
def vectorize(f):
    def newfun(l):
        return list(map(f, l))
    return newfun

def square(x): return x * x
f = vectorize(square)
print(f([1,2,3]))

g = vectorize(len)
print(g(["hello", "world"]))

