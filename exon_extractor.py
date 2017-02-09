#!/usr/bin/env python

import re
import random
from sys import argv

def main(): 
    try:
        ERROR_MESSAGE = "\nAre you a fucking dumb?\n\nHow to use: exon_extractor exon_annotation_file exon_identification sequence_file \ne.g.: exon_extractor my_annotation_file A sequence.fasta\n"        
        annotation_file = open(argv[1], "r")
        exon_identification = argv[2]
        identificator_re = "^.*"+exon_identification+":.*$"
        exon_beginning_re = re.compile("\[\d+")
        exon_ending_re = re.compile("\d+\]")
        sequence = open(argv[3], "r").read()


        for line in annotation_file:
            if re.match(identificator_re, line):                
                exon_beginning = int(exon_beginning_re.findall(line)[0].replace("[",""))-1
                exon_ending = int(exon_ending_re.findall(line)[0].replace("]",""))

        exon_to_remove = sequence[exon_beginning:exon_ending]
        new_sequence = sequence.replace(exon_to_remove, "").replace(" ", "")
        print(new_sequence)
        
    except IOError:
        print("\nCannot find the file(s): "+argv[1]+" or "+argv[3]+"\n"+ERROR_MESSAGE)
    except RuntimeError as e:
        print(e.args[0]+"\n"+ERROR_MESSAGE)
    except (ValueError, IndexError):
        print(ERROR_MESSAGE)

main()
