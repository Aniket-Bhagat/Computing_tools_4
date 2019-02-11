#!/usr/bin/env python

file=open('sun.txt','r')	# Open sun.txt file
l=file.readlines()			# Read lines and store as list

length=[]				# Empty list
for i in l:
	length.append(len(i))	# Store length of each line in Empty list

n=max(length)			# Figure out maximum length from list
print 'Longest line in file is '+str(n)+' charecters long including "\\n"'
print 'Following are the lines having Maximum length\n'

for i in l:
	if n==len(i):		# If line length is equal to maximum length
		print i.strip()	# then print it

file.close()				# Close the file
