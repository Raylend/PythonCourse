"""
Given: Two DNA strings s and t (each of length at most 1 kbp).

Return: All locations of t as a substring of s.
"""
s = input("Input a string s:\n")
t = input("Input a string t:\n")
end = len(s)
r = 0
buf = 0
if t in s:
    while t in s:
        r = s.find(t, r, end)
        s = s[r+1:end]
        print(r + 1 + buf, end=' ')
        buf = buf + r + 1
        r = 0
else:
    print("t is not a substring of s!\n")
    quit()
print("\n")
quit()
