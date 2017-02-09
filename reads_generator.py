#!/usr/bin/env python

import re
import random
from sys import argv

def main(): 
    try:
        ERROR_MESSAGE = "\nAre you a fucking dumb?\n\nHow to use: reads_generator sequence_file read_length how_many_times\ne.g.: reads_generator my_file.fasta 75 100000\n"
        sequence_file = open(argv[1], "r")
        sequence = sequence_file.read()
        read_length = int(argv[2].lower())
        times = int(argv[3].lower())
        
        if (read_length > len(sequence)):
            raise RuntimeError("\nWhat kind of dumb are you? You cannot create a read greater than the sequence!\n")
#        if re.match("^[ACGT]*$", sequence) is None:
#            raise RuntimeError("\nThis sequence is invalid. All characters must be A, C, G or T.")

        for i in range(times):
            max_index = (len(sequence) - read_length)
            index = random.randint(0, max_index)

            print(sequence[index: (index+read_length)])	

    except IOError:
        print("\nCannot find the file: "+argv[1]+"\n"+ERROR_MESSAGE)
    except RuntimeError as e:
        print(e.args[0]+"\n"+ERROR_MESSAGE)
    except (ValueError, IndexError):
        print(ERROR_MESSAGE)

main()
