"""
Counting Point Mutations

Problem

Given two strings s and t of equal length, the Hamming distance
between s and t, denoted dH(s,t), is the number of corresponding symbols
that differ in s and t.

Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).

Return: The Hamming distance dH(s,t).
"""
s = input("Input your first DNA string\n")
t = input("Input your second DNA string\n")
dh = 0
length1 = len(s)
length2 = len(t)
if length1!=length2:
    print("Lengths of your strings are not equal!")
else:
    for i in range(0,length1):
        if s[i]!=t[i]:
            dh = dh + 1

print("The Hamming distance")
print(dh)
