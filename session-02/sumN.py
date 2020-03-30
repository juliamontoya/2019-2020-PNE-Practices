#We need to convert the sum20.py program into a function, and then called it twice, using the arguments n=20 and n=100.
# The code is this:
# Function for calculating the sum of the
# N first integer numbers

# --1 + 2 + 3 +....+20
# - 1 + ....+100

def sum (n):
    res = 0
    for i in range(1, n+1):
        res += i
    return res


print("sum of 1-20:", sum(20))
print("sum of 1-100:", sum(100))