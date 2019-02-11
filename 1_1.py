#!/usr/bin/env python

file=open('sun.txt','r')	# open a file in read mode
l=file.readlines()		# read all lines in file and store as list l
print 'Total no. of lines in file : '+str(len(l))		# print length of l
file.close()		# Close file