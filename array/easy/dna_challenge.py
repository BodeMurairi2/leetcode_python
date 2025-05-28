#!/usr/bin/env python3

complement = {
    "A": "T",
    "G": "C",
    "T": "A",
    "C": "G"
}

dna = "batcdsshagc"

def DNA_strand(dna:str) -> str:
    """This function returns the DNA sequence"""
    new_string = ""
    for i in dna.upper():
        if i in complement.keys():
            new_string += complement[i]
        else:
            new_string += i.upper()
    return new_string.lower()

print(DNA_strand(dna))
