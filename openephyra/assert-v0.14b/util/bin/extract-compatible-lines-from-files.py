#!/bin/python

import sys
import string


if ( len(sys.argv) == 1):
	print "Usage: extract-compatible-lines-from-two-files.py <file1> <file2> <file3> <file1_compare_on> <file2_compare_on> <file1.sync> <file2.sync> <file3.sync>"

input_file_1_lines = open(sys.argv[1]).readlines()
input_file_2_lines = open(sys.argv[2]).readlines()
input_file_3_lines = open(sys.argv[3]).readlines()

input_file_1_compare_lines = open(sys.argv[4]).readlines()
input_file_2_compare_lines = open(sys.argv[5]).readlines()

output_file_1 = open(sys.argv[6], "w")
output_file_2 = open(sys.argv[7], "w")
output_file_3 = open(sys.argv[8], "w")

output_file_1_lines = []
output_file_2_lines = []
output_file_3_lines = []


#---- the two files should be of the same length, else exit ----#
if (len(input_file_1_lines) != len(input_file_2_lines) or len(input_file_1_lines) != len(input_file_3_lines) or len(input_file_2_lines) != len(input_file_3_lines)):
	print "ERROR (%s): The three files should be of the same length" % (sys.argv[0])
	sys.exit()

i=0
count=0
for i in range(0, len(input_file_1_lines)):
	if( input_file_1_compare_lines[i] == input_file_2_compare_lines[i]):
		output_file_1_lines.append(input_file_1_lines[i])
		output_file_2_lines.append(input_file_2_lines[i])
		output_file_3_lines.append(input_file_3_lines[i])
	else:
		count = count + 1
		print "MISMATCH LINE [INDEX ", i, "]"
		print input_file_1_compare_lines[i]
		print input_file_2_compare_lines[i]


#print "REPORT: Had to remove %d lines because of mismatches" % (count)


output_file_1.writelines(output_file_1_lines)
output_file_2.writelines(output_file_2_lines)
output_file_3.writelines(output_file_3_lines)


