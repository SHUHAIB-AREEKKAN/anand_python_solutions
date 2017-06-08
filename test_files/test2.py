n=raw_input('enter triplet value:')
m=int(n)
a=[(x,y,z) for x in range(1,m) for y in range(x,m) for z in range(y,m) if x+y==z]
print a
