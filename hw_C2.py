"""
Посчитать сумму и произведение
цифр положительного числа,
заданного пользователем.
"""

a = input("Enter a positive integer number\n")
try:
    a = int(a)
    if a < 0:
        print("You should have entered a positive integer number.\nAbort session.")
        quit()
    else:
        a = str(a)
        a = list(a)
        sum = 0
        prod= 1
        for e in a:
            sum = sum + int(e)
            prod = prod * int(e)
except ValueError:
    print("You should have entered a positive integer number.\nAbort session.")
    quit()

print(f"The sum of digits in your number: {sum}")
print(f"The product of digits in your number: {prod}")
