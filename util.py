import math
from datetime import datetime

def is_square(n):
    if n < 0: return False
    if n == 0 or n == 1 : return True 
    x = n // 2
    seen = set([x])
    while x*x != n:
        x = (x+(n//x))//2
        if x in seen: return False
        seen.add(x)
    return True

class Helper:
    primes = []
    prime_set = set()
    def is_prime(self, number):
        """
        >>> helper.is_prime(47)
        True
        >>> helper.is_prime(60)
        False
        """
        if number==1 or number == 2 or number == 3:
            return True 
        if number <= 0 or number%2 == 0:
            return False 
        if sum(map(int, str(number)))%3 == 0:
            return False
        if number in self.prime_set:
            return True

        prime_ceiling = int(math.ceil(math.sqrt(number)))
        self.build_primes(prime_ceiling)
        for prime in self.primes:
            if prime == 1:
                continue
            if prime > prime_ceiling: 
                return True 
            if number % prime == 0:
                return False 
        return True

    def next_prime(self, number):
        """
        >>> helper.next_prime(17)
        19
        """
        number+=1
        while not self.is_prime(number):
            number+=1
        return number 

    def prime_divisors(self, number):
        """
        >>> helper.prime_divisors(60)
        {1: 1, 2: 2, 3: 1, 5: 1}
        """
        sqrt_n = int(math.floor(math.sqrt(number)))
        self.build_primes(sqrt_n)
        prime_divisors = {1:1}
        divident = number
        for i in self.primes[1:]:
            if i > math.floor(sqrt_n):
                break
            while divident%i == 0:
                prime_divisors[i] = prime_divisors.get(i, 0)+1
                divident /= i 
        if self.is_prime(divident):
            prime_divisors[divident]=1
        return prime_divisors

    def get_divisors(self, number):
        """
        >>> helper.get_divisors(60)
        [1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60]
        """
        prime_divisors = self.prime_divisors(number)
        divisors = [1]
        del prime_divisors[1]
        for key in prime_divisors:
            new_divisors = []
            for i in divisors:
                for j in range(prime_divisors[key]):
                    new_divisors.append(i*key**(j+1))
            divisors+=new_divisors
        divisors.sort()
        return divisors

    def get_divisors_dumb(self, number):
        """
        >>> helper.get_divisors_dumb(60)
        [1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60]
        """
     
        divisors = []
        for i in range(1, number+1):
            if number%i == 0:
                divisors.append(i)
        return divisors

    def are_relative_primes(self, a, b):
        if a == 1 or b == 1:
            return True
        if a%b == 0 or b%a == 0:
            return False
        self.build_primes(max(a/2,b/2))
        limit = min(a/2, b/2)
        index = 1
        prime = self.primes[index]
        while prime<=limit:
            if a%prime == 0 and b%prime == 0:
                return False
            index+=1
            prime = self.primes[index]
        return True

    def are_relative_primes_slow(self, a, b):
        a_divisors = self.prime_divisors(a)
        del a_divisors[1]
        b_divisors = self.prime_divisors(b)
        for key in a_divisors.keys():
            if b_divisors.get(key) != None:
                return False
        return True
        
    def largest_common_denominator(self, a, b):
        """
        >>> helper.largest_common_denominator(6, 4)
        2
        >>> helper.largest_common_denominator(36, 45)
        9
        """
        a_divisors = self.prime_divisors(a)
        b_divisors = self.prime_divisors(b)
        target = 1
        for i in a_divisors.keys():
            target *= i**min(a_divisors[i], b_divisors.get(i, 0))
        return target
        
    def build_primes(self, limit):
        """
        >>> helper.build_primes(10)
        >>> helper.primes
        [1, 2, 3, 5, 7]
        """
        for i in xrange(self.primes[-1]+1, limit+1):
            if self.is_prime(i):
                self.primes.append(i)
                self.prime_set.add(i)
        
    def __init__(self):
        self.primes = [1,2]

if __name__ == "__main__":
        import doctest
        doctest.testmod(extraglobs={'helper': Helper()})
