#Recursive Sum
def sum(n):
    #base case
    if n == 0:
        return 0
    #recursive case (one or more)
    print(n)
    return n + sum (n - 1)

s = sum(10)
print("sum =", s)