#!/usr/bin/env python

import re								# Importing 'regular expression' module

file=open('names.html',"r")				# Open file in read mode
lines=file.readlines()					# Read each line and store as list

rank={}									# Create an empty dictionary
for line in lines:
	if re.search(r"right",line):		# Regex to search word "right" in line
		s=re.split('<|>',line)			# Split line at position where '<'or'>' is found
		rank[int(s[4])] = []			# For each Kye make list as empty list to append values
		rank[int(s[4])].append(s[8])	# Append first Value for Kye
		rank[int(s[4])].append(s[12])	# Append second Value for Kye

print rank			# Print entire dictionary

file.close()		# Close the file