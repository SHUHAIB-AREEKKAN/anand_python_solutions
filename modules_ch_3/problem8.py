#anand python problem 8 3:8
#Write a program links.py that takes URL of a webpage as argument and prints all the URLs linked from that webpage.

import urllib
import re

def link_in_html(url):
	out=urllib.urlopen(url)
	datas=out.read()
	urls=re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',datas)
	print urls




if __name__ == '__main__':
	link_in_html('http://docs.python.org/')
