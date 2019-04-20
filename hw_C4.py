"""
Пользователь задаёт числа a, b, c
из уравнения ax^2 + bx + c = 0,
вывести корни уравнения или
сообщить, что их нет.
"""

print("This program solves quadratic equations.")
print("You will need to input a, b, c for the equation")
print("ax^2 + bx + c = 0.")

a = input("Input a.\n")
b = input("Input b.\n")
c = input("Input c.\n")

try:
    a = float(a)
    b = float(b)
    c = float(c)
except ValueError:
    print("You should have entered three numbers!\nAbort session.")
    quit()

discriminant = b**2 - 4*a*c
if discriminant < 0:
    print("The equation does not have real solutions!")
else:
    if a!=0:
        x_1 = (-b - discriminant**0.5)/(2*a)
        x_2 = (-b + discriminant**0.5)/(2*a)
        print(f"x_1 = {x_1}")
        print(f"x_2 = {x_2}")
    else:
        if b == 0 and c == 0:
            print("The solution is any of real numbers.")
        elif b!=0:
            x_1 = -c/b
            print(f"x_1 = x_2 = {x_1}")
        elif b==0 and c!=0:
            print("The equation does not have solutions!")
