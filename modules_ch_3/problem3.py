# anand python 3 3:3
#Write a program to list all the files in the given directory along with their length and last modification time. The output should contain one line for each file containing filename, length and modification date separated by tabs.

import os
import sys

def file_info(paths):
        for i in os.listdir(paths):
		print '{} \t {} \t {}'.format(i,os.stat(i).st_size,os.stat(i).st_mtime)
                



if __name__ == '__main__':
         file_info('.')
