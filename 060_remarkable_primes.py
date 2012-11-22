#The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.
#
#Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.
from util import *
helper = Helper()
MAX = 9999

def are_remarkable(a,b):
    if helper.is_prime(int(str(a)+str(b))) and helper.is_prime(int(str(b)+str(a))):
        return True
    return False

def five_remarkables():
    first = 3
    while first < MAX:
        second = helper.next_prime(first)
        while second < MAX:
            if are_remarkable(first, second):
#        print str(first)+" "+str(second)
                third = helper.next_prime(second)
                while third < MAX:
                    if are_remarkable(first, third) and are_remarkable(second, third):
#                    print str(first)+" "+str(second)+" "+str(third)
                        forth = helper.next_prime(third)
                        while forth< MAX:
                            if are_remarkable(first, forth)\
                                and are_remarkable(second, forth)\
                                and are_remarkable(third, forth):
#                            print str(first)+" "+str(second)+" "+str(third)+" "+str(forth)
                                fifth = helper.next_prime(forth)
                                while fifth < MAX:
                                    if are_remarkable(first, fifth)\
                                        and are_remarkable(second, fifth)\
                                        and are_remarkable(third, fifth)\
                                        and are_remarkable(forth, fifth):
#                                    print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
#                                        print str(first)+" "+str(second)+" "+str(third)+" "+str(forth)+" "+str(fifth)
                                        return [first, second, third, forth, fifth]

                                    fifth = helper.next_prime(fifth)
             
                            forth = helper.next_prime(forth)
                    third = helper.next_prime(third)
            second = helper.next_prime(second)
        first = helper.next_prime(first)

#print datetime.now()
#[13, 5197, 5701, 6733, 8389]
print sum(five_remarkables())
#26033
#print datetime.now()
