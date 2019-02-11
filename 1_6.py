#!/usr/bin/env python

file1=open('sun.txt',"r")			# Open file in Read mode
l=file1.readlines()					# Read each line and make list
file2=open('sun_names.txt',"w")		# Open another file in write mode

for i in l:
	file2.writelines(i.strip().split('/')[-1])	# Split each line at '/' and write last element of it
	file2.write('\n')							# print '\n'

print 'File names extracted and written in another file successfully...'
file1.close()		# Close both files
file2.close()		#
