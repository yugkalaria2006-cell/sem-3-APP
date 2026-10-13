#Memoized Recursion
memo = {}
def fibo(n):
    if n <= 1:
        return 1
    if n in memo:
        return memo[n]
    #recursive case
    memo[n] = fibo(n-1)+ fibo(n-2)
    return memo[n]

print(fibo(6))
