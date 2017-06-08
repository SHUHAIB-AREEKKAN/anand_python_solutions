# anand python problem 6 3:6
# Write a program antihtml.py that takes a URL as argument, downloads the html from web and print it after stripping html tags.

#

import os
import sys
import urllib
import re

def html_rem(url):

	if url[-1]=='/':
   		basename='index.html'
	else:
  		sec=url.split('/')
		basename=sec[-1] 
	print ' Saving  ',url,'  as filename ',basename
	urllib.urlretrieve(url,os.path.join(os.getcwd(),basename))
	sec1=re.findall(r'>[^<]+<',open(basename).read())
	print sec
	for i in sec1:
		print i[1:-1]


if __name__ == '__main__':

	html_rem(sys.argv[1])

