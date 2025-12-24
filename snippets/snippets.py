import math
from decimal import getcontext, Decimal

def isPrime(n:int, foundPrimes=None):
    foundPrimes = range(2, int(n**0.5)) if foundPrimes is None else foundPrimes
    for factor in foundPrimes:
        if n % factor == 0:
            return False
    return True

def listPrimes(max: int):
    foundPrimes = []
    for n in range(2, max):
        if isPrime(n, foundPrimes):
            foundPrimes.append(n)
    return foundPrimes

print(listPrimes(10))

print(int(8.999)) # python will round down to 8, use round function
print(round(14/3, 2))

getcontext().prec = 3
print(Decimal(1) / Decimal(3))

cat_name = "my name is fuzzlekins"
print(cat_name[0])
print(cat_name[:7])
print(cat_name[5:])
print(len(cat_name))
print(f"number is {4}") # prior to python 3.6, you had use string.format()
print("Pi is {}".format(math.pi))

print(bytes(4))
print(bytes("😃", "utf-8"))
print(bytes("😃", "utf-8").decode("utf-8"))

def getFactors(n):
    return [factor for factor in range(1, n+1) if n % factor == 0]

print(getFactors(4))
