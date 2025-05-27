#!/usr/bin/env python3

complement = {
    "A": "T",
    "G": "C",
    "T": "A",
    "C": "G"
}

def DNA_strand(dna):
    """This function returns the DNA sequence"""
    new_string = ""
    for i in dna:
        if i.upper() in complement.keys():
            new_string += complement[i.upper()]
        else:
            new_string += i.upper()
    return new_string.lower()
