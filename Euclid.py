

import math
def GCD(a,b):
    if(a ==0):
        return b
    elif(b == 0):
        return a
    if(a > b):
        r = a % b
        return GCD(b, r)
    else:
        r = b % a
        return GCD(a,r)

def getPrimesList(top):
    list_primes = list()


def isPrimeNumber(number):
    if(number == 2 or number == 1):
        return True
    if number % 2 == 0:
        return False
    i = 3
    composingPrimes = []
    while i <= number and i <= math.sqrt(number):
        if(number % i == 0):
            if(len(composingPrimes) > 1):
                return False
            composingPrimes.append(i);
        i += 2
    if(len(composingPrimes) > 1):
        return False
    else: return True

#brute force!!
print("prime? 1-4294967291")
primes = []
every500 = 5000;
for x in range(1,4294967291):
    if(isPrimeNumber(x)):
        primes.append(x)
    numPrimes = len(primes)
    if(numPrimes % every500 == 0):
        print(numPrimes)
        print(x)
print(len(primes))
    #print(str(x)+" "+str(isPrimeNumber(x)))

