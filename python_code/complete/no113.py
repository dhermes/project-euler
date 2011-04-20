from math import factorial

def choose(n, k):
    return factorial(n)/(factorial(k)*factorial(n - k))

n=100
print choose(n+10,10) + choose(n+9,9) - 10*n - 2
