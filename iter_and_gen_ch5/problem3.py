#anand python problem 3 5:3
#Write a function findfiles that recursively descends the directory tree for the specified directory and generates paths of all the files in the tree.
#
import os

def get_path(direc):
	for i in os.listdir(direc):
		paths=os.path.join(direc,i)
		yield paths
def print_path(direc):
	for path in get_path(direc):
		if os.path.isfile(path):
			print path
		else:
			print_path(path)
print_path('.')
	

