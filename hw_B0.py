"""""
Counting DNA Nucleotides

Problem
A string is simply an ordered collection of symbols selected
from some alphabet and formed into a word; the length of a
string is the number of symbols that it contains.

An example of a length 21 DNA string (whose alphabet contains
the symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."

Given: A DNA string s of length at most 1000 nt.

Return: Four integers (separated by spaces) counting the
respective number of times that the symbols 'A', 'C', 'G',
and 'T' occur in s.
"""""
# The beginning
s = input("Input your DNA string s\n")
print("You entered:")
print(s)

number_of_A = 0
number_of_C = 0
number_of_G = 0
number_of_T = 0

for element in s:
    if element=='A':
        number_of_A+=1
    elif element=='C':
        number_of_C+=1
    elif element=='G':
        number_of_G+=1
    elif element=='T':
        number_of_T+=1
answer = "{} {} {} {}".format(number_of_A, number_of_C, number_of_G, number_of_T)
print(answer)

# The alternative

number_of_A = s.count('A')
number_of_C = s.count('C')
number_of_G = s.count('G')
number_of_T = s.count('T')
answer2 = f"{number_of_A} {number_of_C} {number_of_G} {number_of_T}"
print(answer2)
