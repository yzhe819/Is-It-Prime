import random
from .constants import DEFAULT_ROUNDS


# Fermat Primality Test
def _fermat_test(n: int, a: int) -> bool:
    # when n is prime and gcd(a, n) = 1,
    # a^(n-1) = 1 (mod n)
    return pow(a, n - 1, n) == 1


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False

    # fermat test is a kind of probabilistic test
    # for choosing base a, the range will 2 <= a <= n - 2
    # On the real world, we should do mutiple rounds of fermat test
    #  we should choose 40 roundec from 2 to n - 2
    for _ in range(DEFAULT_ROUNDS):
        a = random.randint(2, n - 2)
        if pow(a, n - 1, n) != 1:
            return False

    return True
