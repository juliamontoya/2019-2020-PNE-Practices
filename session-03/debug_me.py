# --- Find the error!


def g(a, b):
    return a - b


def f(a, b, c, d):
    t0 = a + b - g(a, 0)
    t1 = g(c, d)
    t3 = 2 * (t0 / t1)
    return t0 + 2*t1 + t3*t3


# -- Main program
print("Result 1: ", f(5, 2, 5, 0))
print("Result 2: ", f(0, 2, 3, 3))
print("Result 3: ", f(1, 3, 2, 3))
print("Result 4: ", f(1, 9, 22.0, 3))

#Execute the program. what happens?
#it gives an error in the line 11 and 17, but if works in the first result
#Execute it step by step. Could you find where is the problem!
# the error starts in the line 11 because there is a division in the second result t3 = 2 * (t0 / t1) that is a division
#by zero because t1 =0  so it can't be calculate, because of that the error appears algo in the line 17 when you print result 2
# it happens the same with the other results that appears a division by zero  except with the first one.


