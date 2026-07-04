import math


# to check if exists m**k = n
def _is_perfect_power(n: int) -> bool:
    if n < 4:
        return False

    L = n.bit_length()
    for k in range(2, L):
        m = 2
        while m**k <= n:
            if m**k == n:
                return True
            m += 1
    return False


def _find_order(n: int, r: int) -> int:
    n = n % r
    k = 1
    value = n % r
    while value != 1:
        value = (value * n) % r
        k += 1
    return k


def _find_min_r(n: int) -> int:
    threshold = (math.log2(n)) ** 2
    safety_limit = int((math.log2(n)) ** 5) + 100

    r = 2
    # aks supports that the suitable r must exists
    # so the loop will end when the suitable r is found
    while r < safety_limit:
        g = gcd(n, r)

        if 1 < g and g < n:
            raise ValueError(f"n is composite, found factor {g}")

        if g == 1:
            order = _find_order(n, r)
            if order > threshold:
                return r

        r += 1

    #  this should never be targeted
    raise RuntimeError("unexpected: no valid r found within theoretical bound")


def _find_upper_bound_of_a(n: int, r: int) -> int:
    return math.sqrt(r) * math.log2(n)


# AKS Primality Test
def _aks_test(n: int) -> bool:
    if _is_perfect_power(n):
        return False

    r = _find_min_r(n)
    L = _find_upper_bound_of_a(n, r)

    for a in range(1, L + 1):
        if gcd(a, n) > 1:
            return False
        # do the verification here

    return True


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False

    return _aks_test(n)
