#anand python problem 10 3:10
#Write a program myip.py to print the external IP address of the machine. Use the response from http://httpbin.org/get and read the IP address from there. The p#rogram should print only the IP address and nothing else.

import urllib
import json
response=urllib.urlopen('http://httpbin.org/get')
k=json.loads(response.read())["origin"]
print k
