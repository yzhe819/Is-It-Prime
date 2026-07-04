# this implementation is based on the numpy and sympy libray
# only keep the core logic and remove the unnecessary code
import math
import flint
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


# use flint to do the computation rather than half python and half flint
def _verify(a: int, n: int, r: int) -> bool:
    modulus = flint.nmod_poly([0] * r + [1], n) - flint.nmod_poly([1], n)

    base = flint.nmod_poly([a % n, 1], n)
    lhs = base.pow_mod(n, modulus)

    rhs = flint.nmod_poly([0] * (n % r) + [1], n)
    rhs += flint.nmod_poly([a % n], n)

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
