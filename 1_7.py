#!/usr/bin/env python

file=open('sun_names.txt',"r")		# Open file in read mode
l=file.readlines()			# Read each line and store in lists

print 'Checking for Duplicates...'

temp=[]			# Empty list
for i in l:
	if l.count(i)>1:		# Count no of similar entries in list
		temp.append(i)		# If count greater than one then append to empty list

temp=set(temp)				# Make set of empty list
if len(temp)==0:			# If nothing in list print 'No Duplicates'
	print 'No duplicates entries found'
else:
	print 'Duplicate entries are found'				# If any duplicates then print them
	print str(len(temp))+' entrie(s) have duplicates'
	print ''.join(temp)

file.close()	# Close the file