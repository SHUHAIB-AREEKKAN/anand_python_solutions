#anand python probelm 12 3:12
#Write a program mydoc.py to implement the functionality of pydoc. The program should take the module name as argument and print documentation for the module and each of the functions defined in that module.
#
import sys
def mydoc(sec):
	print 'Help on module '+sec
	print'\n\nDESCRIPTION\n'
	__import__(sec)
	print dir(sec)



if __name__ == '__main__':
	mydoc(sys.argv[1])
