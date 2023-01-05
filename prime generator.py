from itertools import count, islice


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