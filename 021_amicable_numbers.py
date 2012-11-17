#Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
#If d(a) = b and d(b) = a, where a  b, then a and b are an amicable pair and each of a and b are called amicable numbers.
#
#For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
#
#Evaluate the sum of all the amicable numbers under 10000.
from util import *

def is_amicable(a):
    helper = Helper()
    a_sum_div = sum(helper.get_divisors(a)) - a
    if a_sum_div < 1 or a_sum_div == a:
        return False
    b_sum_div = sum(helper.get_divisors(a_sum_div)) - a_sum_div
    if b_sum_div == a:
        print "{0}: {1}".format(a, a_sum_div)
        return True
    return False
    
            
total = 0
for i in range(1, 10001):
    if is_amicable(i):
        total+=i
print total
#31626
