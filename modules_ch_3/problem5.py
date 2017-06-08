# anand python problem 5 3:5
# Write a program wget.py to download a given URL. The program should accept a URL as argument, download it and save it with the basename of the URL. If the URL ends with a /, consider the basename as index.html
import os
import sys
import urllib
import re

def wget(url):

	if url[-1]=='/':
   		basename='index.html'
	else:
  		sec=url.split('/')
		basename=sec[-1] 
	print ' Saving  ',url,'  as filename ',basename
	urllib.urlretrieve(url,os.path.join(os.getcwd(),basename))
	


if __name__ == '__main__':

	wget(sys.argv[1])

