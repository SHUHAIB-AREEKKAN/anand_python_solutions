#anand python problem 9 3:9
# Write a regular expression to validate a phone number.

import re

def check_phno(str1):
	sec=re.findall(r'\d{10}',str1)
	if sec:
		print sec
		




if __name__ == '__main__':
	check_phno('9952877336')
	check_phno('hello23red')
