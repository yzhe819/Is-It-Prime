# this implementation is based on the numpy and sympy libray
# only keep the core logic and remove the unnecessary code
import math
import numpy as np
from typing import List
from sympy import perfect_power
from sympy import n_order


def _find_min_r(n: int) -> int:
    threshold = (math.log2(n)) ** 2
    safety_limit = int((math.log2(n)) ** 5) + 100

    r = 2
    # aks supports that the suitable r must exists
    # so the loop will end when the suitable r is found
    while r < safety_limit:
        g = math.gcd(n, r)

        if 1 < g < n:
            raise ValueError(f"n is composite, found factor {g}")

        if g == 1:
            order = n_order(n, r)
            if order > threshold:
                return r

        r += 1

    #  this should never be targeted
    raise RuntimeError("unexpected: no valid r found within theoretical bound")


def _find_upper_bound_of_a(n: int, r: int) -> int:
    return int(math.sqrt(r) * math.log2(n))


def poly_mul(a: List[int], b: List[int], r: int, mod: int) -> List[int]:
    conv = np.convolve(np.array(a, dtype=object), np.array(b, dtype=object))
    poly = [0] * r
    for i, coef in enumerate(conv):
        poly[i % r] = (poly[i % r] + coef) % mod
    return poly


# do the fast exponentiation of the polynomial
def poly_pow(base: List[int], exp: int, r: int, mod: int) -> List[int]:
    result = [0] * r
    result[0] = 1
    base = base[:]

    while exp > 0:
        if exp & 1:
            result = poly_mul(result, base, r, mod)
        base = poly_mul(base, base, r, mod)
        exp >>= 1

    return result


def _verify(a: int, n: int, r: int) -> bool:
    base = [0] * r
    base[0] = a % n
    base[1 % r] = (base[1 % r] + 1) % n
    lhs = poly_pow(base, n, r, n)

    rhs = [0] * r
    rhs[n % r] = (rhs[n % r] + 1) % n
    rhs[0] = (rhs[0] + a) % n

    return lhs == rhs


# AKS Primality Test
def _aks_test(n: int) -> bool:
    if bool(perfect_power(n)):
        return False

    try:
        r = _find_min_r(n)
    except (ValueError, RuntimeError):
        return False

    l = _find_upper_bound_of_a(n, r)

    for a in range(1, l + 1):
        g = math.gcd(a, n)
        if 1 < g < n:
            return False

        # do the verification here
        if not _verify(a, n, r):
            return False

    return True


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    return _aks_test(n)
