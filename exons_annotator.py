#!/usr/bin/env python

import re
import random
from sys import argv

def main(): 
    try:
        sequence_file = open(argv[1], "r")
        sequence = sequence_file.read()
        annotation = {"A":0, "B":0, "C":0}

        annotation["A"] = random.randint(1, int(len(sequence)/3))
        
        max_b = (annotation["A"]+int(len(sequence)/2))
        annotation["B"] = random.randint((annotation["A"]+1), max_b)

        max_c = (annotation["B"] + int(len(sequence)))
        annotation["C"] = random.randint((annotation["B"]+1), max_c)
        
        print("\nExon A: [1, "+str(annotation["A"])+"]\n"+
              "Exon B: ["+str(annotation["A"]+1)+", "+str(annotation["B"])+"]\n"+
              "Exon C: ["+str(annotation["B"]+1)+", "+str(annotation["C"])+"]\n")
              
    except (ValueError, IndexError):
        print("\nAre you a fucking dumb?"+
              "\n\nHow to use: exons_annotator sequence_file \n"+
              "e.g.      : exons_annotator my_fasta_file \n")

main()
