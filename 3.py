#!/usr/bin/env python

file=open('marks.txt',"r")				# Open file in reading mode
l=file.readlines()[1:]					# Read all lines except Header line # Store in list

A=0;B=0;C=0								# Declare Three variables for each subject
print 'Total marks for each student :'
for i in l:
	if i != "\r\n" and i != "\n":		# To skip unnecessary new line charecter
		i = i.strip("\r\n")				# To remove unnecessary new line charecter
		i = i.split("\t")				# Split line with '\t' as delimiter

		A+=float(i[1])	#
		B+=float(i[2])	# Iteratively Add respective subject marks 
		C+=float(i[3])	# 

		s=(float(i[1])+float(i[2])+float(i[3]))	# Sum of all subject for each person
		print i[0]+'\t= '+str(s)

print '\nEach Subject Total :'
print 'A = '+str(A)				# 
print 'B = '+str(B)				# Printing Total marks of each subject
print 'C = '+str(C)				# 
file.close()			# Close file