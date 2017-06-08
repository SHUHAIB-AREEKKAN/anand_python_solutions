# anand python problem 1 3:1
# Write a program to list all files in the given directory.
import os
import sys
paths=sys.argv[1]

print os.listdir(paths)
