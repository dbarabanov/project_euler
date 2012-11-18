#An irrational decimal fraction is created by concatenating the positive integers:
#
#0.123456789101112131415161718192021...
#
#It can be seen that the 12th digit of the fractional part is 1.
#
#If dn represents the nth digit of the fractional part, find the value of the following expression.
#
#d1  d10  d100  d1000  d10000  d100000  d1000000

def digit(n):
    numdigits=1
    while n > 9*10**(numdigits-1)*numdigits:
        n-=9*10**(numdigits-1)*numdigits
        numdigits+=1

    target = 10**(numdigits-1)+(n-1)/numdigits
    digit = (n-1)%numdigits
    return int(str(target)[digit])
   
print reduce(lambda x,y: x*y, [digit(n) for n in [10**i for i in range(7)]])
#210
