#!/usr/bin/env python

file=open('sun.txt','r')	# open a file in read mode
l=file.readlines()		# read all lines in file and store as list l
n=input('How many no. of lines you want to read : ') # Take user input for line numbers

while (n>len(l)):													# Check if no. entered is
	print 'Entered number is greater than total lines in file:'		# greater than lines contained
	n=input('Enter number again : ')								# in given file

for i in range(n):
		print l[i].strip('\n') # Print each line by removing '\n'

file.close()	# Close the file