#!/usr/bin/env python3

"""
Script Name: DNA GC Content Calculator

Description: This script calculates the GC content of a DNA sequence read from a file.
The file should contain only the DNA sequence, and the GC content is rounded to two decimal places.

I wrote this script as part of the exercises I did on the codechalleng.es platform. While I will focus my
efforts on using Python in a cybersecurity setting, I thought it could be nice to do this exercise
because I have actual experience with DNA, Biotechnology, and labs from previous academic and
professional experiences. I wanted to reference that part of my life with this Python exercise.


Usage: python script_name.py <filepath>

Author: Harpocrat3s

Date: 2023-05-09
"""

def calculate_gc_content(sequence):
    """
    Receives a DNA sequence (A, G, C, or T) as input
    Returns the percentage of GC content (rounded to two decimal places)
    """
    VALID_BASES = 'gcat'

    gc_count = 0
    total_bases = 0

    for line in sequence:
        for b in line:
            if b.lower() in VALID_BASES:
                gc_count += (b.lower() == 'g' or b.lower() == 'c')
                total_bases += 1
            else:
                continue  # Skip unknown bases

    gc_content = (gc_count / total_bases) * 100 if total_bases > 0 else 0

    return round(gc_content, 2)


def read_dna_from_file(filepath):
    """
    Reads the DNA sequence from a file and calculates the GC content.
    The file will need to have just the sequence of DNA.
    Prints the DNA sequence and the GC content to the console.
    """
    with open(filepath, "r") as file_object:
        lines = file_object.readlines()

    sequence = "".join(line.strip() for line in lines)

    print("DNA sequence:", sequence)
    print("GC content:", calculate_gc_content(sequence))


if __name__ == '__main__':
    # This allows the script to be run from the command line with an argument
    import sys

    if len(sys.argv) < 2:
        print("Usage: python script.py <filepath>")
        sys.exit(1)

    read_dna_from_file(sys.argv[1])
