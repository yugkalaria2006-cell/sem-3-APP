#Recursive Factorial
def factorial(n):
    #base case
    if n == 0:
        return 1
    #recursive case (one or more)
    print(n)
    return n * factorial (n - 1)

f = factorial(998)
print("factorail =", f)