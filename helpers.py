from collections import defaultdict

def fib(limit=None):
    a, b = 1, 2
    if limit is None:
        limit = float('Inf')
    while a < limit:
        yield a
        a, b = b, a + b
        

def prime_sieve(limit):
    prime_list = defaultdict(lambda: True)
    prime_list[0] = False
    prime_list[1] = False
    for i in range(limit):
        if prime_list[i] == False:
            continue
        yield i
        for j in range(2*i, limit, i):
            prime_list[j] = False
            
            
def prime_factors(num, primes=None):
    if primes == None:
        primes = prime_sieve(num + 1)
    factors = filter(lambda x: num % x == 0, primes)
    yield from factors