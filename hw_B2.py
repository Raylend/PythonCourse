"""
Complementing a Strand of DNA


Problem
In DNA strings, symbols 'A' and 'T' are complements of each other, as are
'C' and 'G'.

The reverse complement of a DNA string s is the string sc formed by
reversing the symbols of s, then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").

Given: A DNA string s of length at most 1000 bp.

Return: The reverse complement sc of s.
"""
s = input("Input your DNA string\n")
t = s[::-1]
sc = ""
for element in t:
    if element=='A':
        sc = sc + 'T'
    elif element=='T':
        sc = sc + 'A'
    elif element=='C':
        sc = sc + 'G'
    elif element=='G':
        sc = sc + 'C'
print("The reverse complement")
print(sc)
