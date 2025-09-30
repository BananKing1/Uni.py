# Fibonacci

# declare how many sequences
n = int(input("How many sequence? "))


# declare a and b
a, b = 1, 1

# this will print a and b and the sum of (a+b)on the same line
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b




