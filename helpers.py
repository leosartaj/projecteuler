import string
from collections import defaultdict
from itertools import chain

alpha_to_val_map = {alp: ord(alp.upper()) - 64 for alp in chain(string.ascii_uppercase, string.ascii_lowercase)}
alpha_to_val = lambda alp: alpha_to_val_map[alp]


def word_value(word):
    vals = map(alpha_to_val, word)
    value = sum(vals)
    return value


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


def is_palindrome(num):
    num = str(num)
    return num == num[::-1]


def dec_to_binstr(num):
    return bin(num)[2:]
