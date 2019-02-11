#!/usr/bin/env python

file1=open('sun.txt',"r")			# Open a file 'sun.txt' in read mode
file2=open('sun_copy.txt',"w")		# Open another file for copying in write mode
l=file1.read()						# Read file1 and store the content in variable

file2.write(l)		# Write content of file1 in file2

print 'File copied successfully...'
file1.close()		# Close file1
file2.close()		# Close file2
