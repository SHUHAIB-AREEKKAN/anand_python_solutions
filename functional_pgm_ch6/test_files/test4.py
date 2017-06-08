
permutation_list = []
def permute(list_, left = 0, right = None):
    if left == right:
        permutation_list.append(list_[:])
    else:
        for i in range(left, len(list_)):
            list_[left], list_[i] = list_[i], list_[left]
            permute(list_, left+1, len(list_))
            list_[left], list_[i] = list_[i], list_[left]
    return permutation_list

def counts(sec):
	return len(sec)
def onecount(sec):
	cc=0
	for i in sec:
		 if i[0]=='2':
			cc+=1
	return cc
			


print onecount(permute(list('12345')))

print counts(permute(list('12345')))
