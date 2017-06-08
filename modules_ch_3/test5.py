#
#

import os

a='|--'
b='|  '
c='\--'

def directory_tree(dire,v=0):
	#print os.listdir(dire)
	names=os.listdir(dire)

	for i in names:
		#print 'the v :'+str(v)
		if os.path.isdir(os.path.join(dire,i)):
			if i == names[-1]:
				print b*v+c+i
			else:	
				print b*v+a+i

			directory_tree(os.path.join(dire,i),v+1)
		if i == names[-1]:
			print b*v+c+i
		else:	
			print b*v+a+i





if __name__ == '__main__':

	directory_tree('/home/shuhaib/anand_python/modules_ch_3/')

