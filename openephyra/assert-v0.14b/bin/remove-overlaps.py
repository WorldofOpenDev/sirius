#!/bin/python
import string
import sys
import re
import os

TRUE  = 1
FALSE = 0
DEBUG = FALSE
OVERLAP_FLAG = FALSE;


if( len(sys.argv) == 1 ):
	print "Usage: remove-overlaps.py <svm-scores-file>"
	sys.exit(1)

score_file_lines       = open(sys.argv[1]).readlines()

score_array            = []
end_array              = []
start_array            = []
list_of_start_arrays   = []
list_of_end_arrays     = []
list_of_constit_arrays = []
list_of_score_arrays   = []
list_of_hyp_arrays     = []
list_of_ref_arrays     = []
list_of_score_lines    = []
score_hash             = {}

if( len(score_file_lines) == 0 ):
	#--- print there are no constituents to analyze ---#

	start_array.append(string.atoi("0"))
	end_array.append(string.atoi("0"))

	sys.exit(0)

start_array = []
end_array   = []
ref_array   = []
hyp_array   = []
score_array = []
score_lines = []

#--- find out the index of ref and hyp columns and the index of the first after hyp ---#
some_list   = string.split(score_file_lines[0])

i= len(some_list) - 1
start_score_index = len(some_list) - 1
hyp_index         = len(some_list) - 1
ref_index         = len(some_list) - 1
#print >>sys.stderr, i

while( i > 0  ):
	if( len(re.findall(r"/",some_list[i])) == 1 ):
		#print >>sys.stderr, i
		#print >>sys.stderr, some_list[i]
		#print >>sys.stderr, re.findall(r"/",some_list[i])
		hyp_index         = hyp_index - 1
		start_score_index = hyp_index + 1
		ref_index         = hyp_index - 1
	else:
		break
	i = i - 1

#print >>sys.stderr, "ref_index:", ref_index
#print >>sys.stderr, "hyp_index:", hyp_index
#print >>sys.stderr, "start_score_index:", start_score_index

#  #--- delete all the lines in the score lines that contain both the hypothesis and the reference as null ---#
#  score_file_lines_no_nulls = []
#  o=0
#  for o in range(0, len(score_file_lines)):
#  	if( len(string.strip(score_file_lines[o])) == 0 ):
#  		score_file_lines_no_nulls.append(score_file_lines[o])
#  		continue

#  	token_list = string.split(score_file_lines[o])

#  	if( token_list[hyp_index] == "O" and token_list[ref_index] == "O" ):
#  		continue
#  	else:
#  		score_file_lines_no_nulls.append(score_file_lines[o])


NON_NULL_FLAG = FALSE
score_file_lines_no_nulls = []
o=0
for o in range(0, len(score_file_lines)):
	if( len(string.strip(score_file_lines[o])) == 0 ):
		if( NON_NULL_FLAG == FALSE ):
			#--- add a dummy one example for this sentence ---#
			score_file_lines_no_nulls.append(some_null_hyp_ref_line)

		#--- then add the blank line ---#
	   	score_file_lines_no_nulls.append(score_file_lines[o])

		NON_NULL_FLAG = FALSE
		continue

	token_list = string.split(score_file_lines[o])

	if( token_list[hyp_index] == "O" and token_list[ref_index] == "O" ):
		some_null_hyp_ref_line = score_file_lines[o]
		continue
	else:
		NON_NULL_FLAG = TRUE
		score_file_lines_no_nulls.append(score_file_lines[o])

score_file_lines = [] + score_file_lines_no_nulls 

for line in score_file_lines:
	if(len(string.strip(line)) == 0):
		#start_array.append(1000)
		#end_array.append(1000)
		#ref_array.append("")
		#hyp_array.append("")
		#score_array.append(1000)
		list_of_start_arrays.append(start_array)
		list_of_end_arrays.append(end_array)
		list_of_score_arrays.append(score_array)
		list_of_hyp_arrays.append(hyp_array)
		list_of_ref_arrays.append(ref_array)
		list_of_score_lines.append(score_lines)

		start_array = []
		end_array   = []
		score_array = []
		hyp_array   = []
		ref_array   = []
		score_lines = []
		
		continue
	
	list = string.split(line)

	#--- store the scores of all the roles in a hash ---#
	j=0
	for j in range(start_score_index, len(list)):
		#print string.split(list[j], "/")[0]
		#print string.split(list[j], "/")[1]
		score_hash[string.split(list[j], "/")[0]] = string.atof(string.split(list[j], "/")[1])
		
	start_array.append(string.atoi(list[2]))
	end_array.append(string.atoi(list[3]))
	ref_array.append(list[ref_index])
	hyp_array.append(list[hyp_index])
	score_array.append(score_hash[list[hyp_index]])
	score_lines.append(line)

if( DEBUG == TRUE ):
	print list_of_ref_arrays
	print list_of_hyp_arrays
	print list_of_start_arrays
	print list_of_end_arrays
	print list_of_score_arrays
	#print list_of_score_lines

#sys.exit(1)
#print start_array
#print end_array

#print list_of_start_arrays
#print list_of_end_arrays

list_of_pruned_start_arrays = []
list_of_pruned_end_arrays   = []
copy_pruned_start_array     = []
copy_pruned_end_array       = []


ii=0
for ii in range(0, len(list_of_score_arrays)):
	if( DEBUG == TRUE ):
		print "sentence index:", ii

	pruned_start_array   = []
	pruned_end_array     = []
	pruned_constit_array = []
	constit_scores       = []
	pruned_score_lines   = []
	pruned_ref_array     = []
	pruned_hyp_array     = []

	pruned_start_array = pruned_start_array + list_of_start_arrays[ii]
	pruned_end_array   = pruned_end_array   + list_of_end_arrays[ii]
	constit_scores     = constit_scores + list_of_score_arrays[ii]
	pruned_score_lines = pruned_score_lines + list_of_score_lines[ii]
	pruned_hyp_array   = pruned_hyp_array + list_of_hyp_arrays[ii]
	pruned_ref_array   = pruned_ref_array + list_of_ref_arrays[ii]
	
	if( DEBUG == TRUE ):
		print pruned_start_array
		print pruned_end_array
	
	copy_pruned_start_array = pruned_start_array
	copy_pruned_end_array   = pruned_end_array

	some_large_index = 1000
	#-- we not have all the arrays to perform overlap removal ---#
	OVERLAP_FLAG = TRUE

	while( OVERLAP_FLAG == TRUE ):
		OVERLAP_FLAG = FALSE

		i=0
		while( i < len(copy_pruned_start_array) - 1 ):
			if( DEBUG == TRUE ):
				print "i:", i
				print copy_pruned_start_array
				print copy_pruned_end_array

			if( copy_pruned_start_array[i+1] > copy_pruned_start_array[i] ):
				if( (copy_pruned_start_array[i+1] > copy_pruned_end_array[i]) and  (copy_pruned_end_array[i+1] > copy_pruned_end_array[i]) ):
					if( DEBUG == TRUE ):
						print "not overlapping"
					i = i + 1
				else:
					#--- found an overlapping pair -- the one with the lesser distance will be pruned ---#
					if( DEBUG == TRUE ):
						print "found an overlapping pair.."
					if( constit_scores[i] < constit_scores[i+1]):
						index = i
					else:
						index = i+1

					if( pruned_ref_array[index] == "O" ):
						if( DEBUG == TRUE ):
							print "corresponding tagged array element for index is null\n";
						del pruned_hyp_array[index]
						del copy_pruned_start_array[index]
						del copy_pruned_end_array[index]
						#del copy_pruned_constit_array[index]
						del score_file_lines[index]
						del constit_scores[index]
						del pruned_ref_array[index]
						del pruned_score_lines[index]
					else:
						if( DEBUG == TRUE ):
							print "corresponding tagged array elemenet for index is not null\n"
						some_large_index = some_large_index + 1
						pruned_hyp_array[index] = "O"
						copy_pruned_start_array[index] = some_large_index
						copy_pruned_end_array[index]   = some_large_index
						constit_scores[index]   = 0
						#--- now lets change the hypothesis to null in the score file ---#
						pruned_score_tokens = string.split(pruned_score_lines[index])
						pruned_score_tokens[hyp_index] = "O"
						pruned_score_lines[index] = "%s\n" % (string.join(pruned_score_tokens, "\t"))
						
					OVERLAP_FLAG = TRUE
					break
			else:
				if( (copy_pruned_start_array[i] > copy_pruned_end_array[i+1]) and (copy_pruned_end_array[i] > copy_pruned_end_array[i+1]) ):
					if( DEBUG == TRUE ):
						print "not overlapping"
					i = i + 1					
				else:
					if( DEBUG == TRUE ):
						print "found an overlapping pair"
					if( constit_scores[i] < constit_scores[i+1] ):
						index = i
					else:
						index = i+1
						
					if( pruned_ref_array[index] == "O" ):
						if( DEBUG == TRUE ):
							print "corresponding tagged array element for index is null\n"
						del pruned_hyp_array[index]
						del copy_pruned_start_array[index]
						del copy_pruned_end_array[index]
						#del copy_pruned_constit_array[index]
						del score_file_lines[index]
						del constit_scores[index]
						del pruned_ref_array[index]
						del pruned_score_lines[index]
					else:
						if( DEBUG == TRUE ):
							print "correspondng taged array element for index is not null\n";
						some_large_index = some_large_index + 1
						pruned_hyp_array[index] = "O"
						copy_pruned_start_array[index] = some_large_index
						copy_pruned_end_array[index] = some_large_index
						constit_scores[index] = 0
						#--- now lets change the hypothesis to null in the score file ---#
						pruned_score_tokens = string.split(pruned_score_lines[index])
						pruned_score_tokens[hyp_index] = "O"
						pruned_score_lines[index] = "%s\n" % (string.join(pruned_score_tokens, "\t"))
										 

					OVERLAP_FLAG = TRUE
					break

	#print " NULL |%s| |%s| " % (string.join(ref_array, "|"), string.join(hyp_array, "|"))
	print string.join(pruned_score_lines, "")
	#sys.exit(1)

