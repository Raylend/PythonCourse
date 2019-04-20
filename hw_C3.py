"""
Определить длину самого короткого
слова в строке, заданной пользователем.
"""
string = input("Input a string\n")
string = string.strip(".,?!:").lower()
a = string.split(" ")
print (a)

length = len(a[0])
for i in range(0, len(a)):
    if length > len(a[i]):
        length = len(a[i])
    else:
        pass

print(f"The length of the shortest word is {length} symbols")
