#!/usr/bin/env python
#!-*- coding: utf8 -*-

import re
import random
from sys import argv

def main(): 
    try:
	# depreceated
	#EXON_AVERAGE_SIZE = 150
	ERROR_MESSAGE = "\nAre you a fucking dumb?\n\nHow to use: remover sequence_file \ne.g.:       remover my_sequence_file.my_extension\n"	

	sequence_file = open(argv[1], "r")
	sequence = sequence_file.read()
	
	# Why have I used 0.00270% of a sequence? Because in (COMPLETE THIS FUCKING THING HERE)
	exons_to_remove = len(sequence)*0.00270/100
        	
	for i in range(exons_to_remove):
	   sequence = sequence.replace(sequence, sequence[0:len(sequence)-150]) 
	
	for read in reads:
	   print(read)	

    except IOError:
	print "\nCannot find the file: "+argv[1]+"\n"+ERROR_MESSAGE
    except RuntimeError as e:
	print e.args[0]+"\n"+ERROR_MESSAGE

    except (ValueError, IndexError):
        print(ERROR_MESSAGE)

main()
