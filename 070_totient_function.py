#Euler's Totient function, tot(n) [sometimes called the phi function], is used to determine the number of positive numbers less than or equal to n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, tot(9)=6.
#The number 1 is considered to be relatively prime to every positive number, so tot(1)=1.
#
#Interestingly, tot(87109)=79180, and it can be seen that 87109 is a permutation of 79180.
#
#Find the value of n, 1  n  107, for which tot(n) is a permutation of n and the ratio n/tot(n) produces a minimum.
from util import Helper
from datetime import datetime
import math
helper = Helper()
MAX = 10000000
helper.build_primes(int(math.sqrt(MAX)))
def totient(n):
    primes = helper.prime_divisors(n)
    del primes[1]
    total = n-1
    for prime in primes.keys():
        count = n/prime-1
        total -= count 
    return total

def is_permutation(a,b):
    return sorted(list(str(a))) == sorted(list(str(b)))

best = 1000
now = datetime.now()
for i in range(MAX*831/1000,MAX*832/1000):
    tot = totient(i)
    if is_permutation(i, tot):
        ratio = float(i)/tot
#        print i
        if ratio < best:
            best = ratio
            best_n = i 
#            print i
#            print ratio
#1.00070905112

#print datetime.now()-now

print best_n 
#8319823
            
