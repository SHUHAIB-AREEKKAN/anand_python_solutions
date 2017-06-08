#anad python problem 2: 27  
#Write a function triplets that takes a number n as argument and returns a list of triplets such that sum of first two elements of the triplet equals the third element using numbers below n. Please note that (a, b, c) and (b, a, c) represent same triplet.
#
#

def triplet(n):
	res=[(x,y,z) for x in range(1,n) for y in range(1,n) for z in range(1,n) if x+y==z ]
	
	
	return res

def imp_triplet(m):
	a=[(x,y,z) for x in range(1,m) for y in range(x,m) for z in range(y,m) if x+y==z]
	return a





def checks(a):
	tmp1=[]
	emp=[]
        for i in range(len(a)):
                for k in range(i+1,len(a)):
                        if (a[i][0]==a[k][0] and a[i][1]==a[k][1]) or (a[i][0]==a[k][1] and a[i][1]==a[k][1]):
                                tmp1.append(a.index(a[k]))
        for ks in a:
                if a.index(ks) in tmp1:
                        print
                else:
                        emp.append(ks)
        return emp



if __name__ =='__main__':
	res2=triplet(5)
	print res2
	print('removing same values ')
	res3=checks(res2)
	print res3
	print imp_triplet(5)	
