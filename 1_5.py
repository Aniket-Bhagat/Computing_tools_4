#!/usr/bin/env python

file1=open('sun.txt',"r")			# Open a file 'sun.txt' in read mode
file2=open('sun_rev.txt',"w")		# Open another file in write mode
l=file1.readlines()					# Read each line and store it as list

for i in l:
	i=i.strip()[::-1]		# Remove '\n' from end and reverse the string
	file2.writelines(i)		# Write reversed string in file2
	file2.write('\n')		# Write '\n' at end of each line

print 'Reversed lines are written successfully in another file...'
file1.close()		# Close file1
file2.close()		# Close file2
