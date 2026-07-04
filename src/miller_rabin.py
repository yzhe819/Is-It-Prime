import random
from .constants import DEFAULT_ROUNDS


# Miller-Rabin Primality Test
def _miller_rabin_test(n: int, a: int, d: int, s: int) -> bool:
    # Miller-Rabin has the squaring chain formula:
    #   a^d, a^(2d), a^(4d), ..., a^(2^(s-1) * d)   [all mod n]

    # for a prime n, this chain must either:
    #   1. start at 1 (a^d = 1 mod n), or
    #   2. hit -1 at some point before reaching the end
    # if neither happens, n is composite.
    x = pow(a, d, n)
    if x == 1 or x == n - 1:
        return True

    for _ in range(s - 1):
        x = pow(x, 2, n)
        if x == n - 1:
            return True

    return False


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False

    # for the given number n,
    # write n - 1 as 2^r * d, where d is odd
    d = n - 1
    r = 0

    # continue halving d until d is odd
    while d % 2 == 0:
        d //= 2
        r += 1

    # miller rabin is also a kind of probabilistic test
    # we should choose 40 rounds from 2 to n - 2
    # and after k rounds, the probability of n being composite is at most (1/4)^k
    for _ in range(DEFAULT_ROUNDS):
        a = random.randint(2, n - 2)
        if not _miller_rabin_test(n, a, d, r):
            return False

    return True
