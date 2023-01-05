from itertools import count, islice
"""Itertools.islice() - Performs lazy slicing of an iterator
Itertools.count() - Lazily generates a sequence of infinite numbers

To find the first N primes, it is possible to create a generator that will produce an infinite sequence of integers 
with itertools.count(), pass these through a generator expression that checks weather each integer is a prime 
using an external function and then use itertools.islice() to capture the slice required slice
This creates a generator object that can then be force evaluated using the list() constructor
"""

def is_prime(x):
    if x > 2:
        for n in range(2, x):
            if x % n == 0:
                return False
        return True
    else:
        return False


y = int(input("how many primes to compute?: "))

print(list(islice((x for x in count() if is_prime(x)), y)))