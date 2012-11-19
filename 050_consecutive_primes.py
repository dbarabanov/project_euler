#The prime 41, can be written as the sum of six consecutive primes:
#
#41 = 2 + 3 + 5 + 7 + 11 + 13
#This is the longest sum of consecutive primes that adds to a prime below one-hundred.
#
#The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.
#
#Which prime, below one-million, can be written as the sum of the most consecutive primes?
from util import *
from datetime import datetime
helper = Helper()
now = datetime.now()
n=1000000
helper.build_primes(n)
primes = helper.primes


max_window = (0,0) 
i=primes[-1]
index = 0
while index<500:
    index+=1
    i=primes[-index]
    low, high = 0,1
    window_sum, window_size = 3, 2
    while low<high:
        if window_sum >= i:
            window_sum -= primes[low]
            low+=1
            window_size -= 1
        elif window_sum <i:
            high+=1
            window_sum += primes[high]
            window_size += 1
        if window_sum == i and window_size > max_window[1]:
#            print "{0}: {1}-{2}. sum:{3} size:{4}".format(i, primes[low],primes[high],window_sum,window_size)
            max_window = (i, window_size)
print max_window[0]
#997651
