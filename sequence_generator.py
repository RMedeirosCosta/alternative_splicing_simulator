#!/usr/bin/env python
#!-*- coding: utf8 -*-

import re
import random
from sys import argv

# Size in bytes you dumbass
def generate_sequence(size):    
    nitrogenous_bases = ("A", "C", "T", "G")
    sequence = ""
    
    for i in range(size):
	sequence += nitrogenous_bases[random.randint(0, 3)]
    
    return sequence

def convert_size(size, unit):
    # 1  Byte = 8 bits
    # 1 Kilobyte (ou KB) = 1024 bytes
    # 1 Megabyte (ou MB) = 1024 kilobytes
    # 1 Gigabyte (ou GB) = 1024 megabytes
    # 1 Terabyte (ou TB) = 1024 gigabytes
    # 1 Petabyte (ou PB) = 1024 terabytes
    # 1 Exabyte (ou EB) = 1024 petabytes
    # 1 Zettabyte (ou ZB) = 1024 exabytes
    # 1 Yottabyte (ou YB) = 1024 zettabytes

    units = ("^bytes?$",".*(kilo|kb).*",".*(mega|mb).*",".*(giga|gb).*", ".*(tera|tb).*",".*(peta|pb).*",".*(exa|eb).*",".*(zetta|zb).*",".*(yotta|yb).*")

    for i in range(len(units)):
	if re.match(units[i], unit) is not None:
		return int(size * (1024**i))

def main(): 
    try:
	size = int(argv[1].lower())
        unit = argv[2].lower()
	print generate_sequence(convert_size(size, unit))

    except (ValueError, IndexError):
        print("\nAre you a fucking dumb?"+
            "\n\nHow to use: sequence_generator size unit\n"+
                "e.g.      : sequence_generator 2 MB\n")

main()
