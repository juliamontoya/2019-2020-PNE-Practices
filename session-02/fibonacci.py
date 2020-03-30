#Write a program(without creating any function) that prints on the console the first 11 terms
# of the fibonacci series (starting from 0)

n= 11
a, b = 0, 1

for i in range (n):
    print(a, end=' ')
    a, b = b, a + b
