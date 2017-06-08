#anand python problem 3 6:3
# Write a function unflatten_dict to do reverse of flatten_dict.

def unflatten_dict(dicts,result=None,tmp=None):
	if result is None:
		result={}
	if tmp is None:  # miniature to carry a {x:2 y:3}
		tmp={}

	for key in dicts:
		if '.' in key:
			tmp[key.split('.')[1]]=dicts[key]
			parent=key.split('.')[0]
			result[parent]=tmp

		else:
			result[key]=dicts[key]
	return result	
if __name__ == '__main__':
	print unflatten_dict({'a': 1, 'b.x': 2, 'b.y': 3, 'c': 4})
