#!/usr/bin/env python

fileA=open('file_A.txt',"r")	# Open both files in read mode
fileB=open('file_B.txt',"r")	# 
listA=fileA.readlines()		# Read each line and store in seperate lists
listB=fileB.readlines()		#

comnum=[]					# Empty list to append common numbers
for i in listA:
	if i in listB:			# Check if number in fileA is present in fileB or not
		comnum.append(i.strip()) # If present append to empty list

print 'Common set of number in both files is :\n'+str(comnum) # print list

fileA.close()	# Close both files
fileB.close()	#