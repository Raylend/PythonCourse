"""
 Пользователь задаёт список чисел,
 выведите все элементы списка,
 которые больше предыдущего элемента
"""
list = []
t = input("Input your first number or a list of numbers in format x, y, z, ...\nThen press ENTER.\n")
if len(t) == 1:
    t = float(t)
    list.append(t)
    while t!="":
        t = input("Enter another number or just press ENTER to finish entering numbers\n")
        if t!="":
            t = float(t)
            list.append(t)
    for i in range(len(list)):
        for j in range(i, len(list)):
            if list[j] > list[i]:
                print(list[j])
    quit()
elif len(t) == 0:
    print("You had to input smth!")
    quit()
elif len(t) > 1:
    t = t.split(", ")
    for i in t:
        i = float(i)
        list.append(i)
    for i in range(len(list)):
        for j in range(i, len(list)):
            if list[j] > list[i]:
                print(list[j])
    quit()
