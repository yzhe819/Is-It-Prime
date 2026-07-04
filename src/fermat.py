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
    # but here we only use the minimum prime number 2 with single round
    # On the real world, we should do mutiple rounds of fermat test
    a = 2
    return _fermat_test(n, a)
