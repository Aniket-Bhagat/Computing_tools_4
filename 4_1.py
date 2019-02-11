#!/usr/bin/env python

import re								# Importing 'regular expression' module

file=open('names.html',"r")				# Open file in read mode
lines=file.readlines()					# Read each line and store as list

for line in lines:
	if re.search(r"right",line):		# Regex to search word "right" in line
		s=re.split('<|>',line)			# Split line at position where '<'or'>' is found
		print s[4]+'\t'+s[8]+'\t'+s[12]	# Print element of index-4(Rank),index-8(Male Name) and index-12(Female Name)

file.close()		# Close the file