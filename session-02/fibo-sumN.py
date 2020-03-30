#Write a function called fibosum(n) that calculates the sum of the n first fibonacci terms.
# The main program should call this function twices, with the arguments n=5 and n=10

def fibosum(n):
    a, b = 0, 1
    sum = 0
    for i in range(n):
        a, b = b, a + b
        sum = a + b
    return sum


print("sum of the first 5 terms of the fibonacci series", fibosum(5))
print("sum of the first 10 terms of the fibonacci series", fibosum(10))