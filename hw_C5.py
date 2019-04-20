"""
Given: Positive integers n≤40 and k≤5.

Return: The total number of rabbit pairs that will be present after n
months, if we begin with 1 pair and in each generation, every pair of
reproduction-age rabbits produces a litter of k rabbit pairs (instead of
only 1 pair).
"""
n = int(input("Input the number of months n\n"))
k = int(input("Input the volume of the litter (number of litter pairs) k\n"))
def fibonacci(number, litter):
    a, b = 1, 1
    for i in range(number):
        yield a
        a, b = b, litter*a + b

r = []
for curr in fibonacci(n, k):
    r.append(curr)
    print(curr)

print(f"The total number of rabbit pairs that will be present after n months is\n{r[n-1]}\n")
quit()
