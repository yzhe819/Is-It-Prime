# Trial Division Primality Test (n >= 3)
def _trial_division_test(n: int) -> bool:
    i = 3
    # use i * i <= n to avoid the calculation of the square root of n
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def is_prime(n: int) -> bool:
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    return _trial_division_test(n)
