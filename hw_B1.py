"""
Transcribing DNA into RNA

Problem
An RNA string is a string formed from the alphabet containing 'A', 'C',
'G', and 'U'.

Given a DNA string t corresponding to a coding strand, its transcribed
RNA string u is formed by replacing all occurrences of 'T' in t with 'U'
in u.

Given: A DNA string t having length at most 1000 nt.

Return: The transcribed RNA string of t.
"""
s = input("Enter your DNA string and I will transform it into the RNA string\n")
t = ""
for element in s:
    if element=='T':
        t = t + 'U'
    else:
        t = t + element

print("RNA string")
print(t)
