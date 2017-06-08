import os
import sys

b='|   '
i=0
def dirtree(base,i):
	filenames=os.listdir(base)
	for filename in filenames:
		if not os.path.isdir(os.path.join(base,filename)):
			if filename==filenames[-1]:
				print b*i+'\--',filename
			else:
				print b*i+'|--',filename
		else:
			print b*i+'|--',filename
			dirtree(os.path.join(base,filename),i+1)






if __name__ == '__main__':
	dirtree(sys.argv[1],i)
