#anand python problem 9 6:9
#Write a function permute to compute all possible permutations of elements of a given list.
#

def permute(lists):
	#print lists
	res=[]
	if len(lists)==1:
		res.append(lists)
	else:
		for i in range(len(lists)):
			print 'the exc',i,len(lists)
			print  'inputs',lists[0:i],'+',lists[i+1:len(lists)]
			perm=permute(lists[0:i]+lists[i+1:len(lists)])
			for k in perm:
				res.append(lists[i]+k)
	return list(set(res))
				

	


if __name__ == '__main__':
	cnt=0
	a=permute('12345')
	#print a
	for  i in a:
		if i[0] == 1 or i[0] == '1':
			cnt+=1
	print cnt
	print len(a)
	print sorted(a)	
