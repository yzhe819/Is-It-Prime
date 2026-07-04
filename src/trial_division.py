# Trial Division Primality Test
def _trial_division_test(n: int) -> bool:
    i = 3
    # use i * i <= n to avoid the calculation of the square root of n
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    return _trial_division_test(n)
