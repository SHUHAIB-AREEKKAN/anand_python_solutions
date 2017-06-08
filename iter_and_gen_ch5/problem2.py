# anand python problem2 5:2
#Write a program that takes one or more filenames as arguments and prints all the lines which are longer than 40 characters.
#
def readfiles(filenames):
	for name in filenames:
		for line in open(name):
			yield line

def line_of_40(lines):
	return (line for line in lines if len(line)>=40)


def print_lines(lines):
	for line in lines:
		print line,

def main(filenames):
	line=readfiles(filenames)
	line=line_of_40(line)
	print_lines(line)
if __name__ == '__main__':

	main(['first.txt','two.txt'])				
