#print 8*9*5*7
#print 16*9*5*7*11*13*17*19
from util import *
helper = Helper()
target = 1
for i in range(2, 21):
    if target%i != 0:
        target *= i/helper.largest_common_denominator(target, i)
print target
#232792560
