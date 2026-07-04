from src.trial_division import is_prime as is_prime_trial_division
from src.miller_rabin import is_prime as is_prime_miller_rabin
from src.miller_rabin_parallel import is_prime as is_prime_miller_rabin_parallel
from src.aks_fast import is_prime as is_prime_aks_fast

# Frank Nelson Cole tooks three years sundays to check the primality of 2^67 - 1
# then he proved that 2^67 - 1 is not a prime number
# 193,707,721 × 761,838,257,287 = 2^67 - 1

M61 = 2**61 - 1


def test_mersenne_M61_by_trial_division():
    assert is_prime_trial_division(M61) is True


def test_mersenne_M61_by_miller_rabin():
    assert is_prime_miller_rabin(M61) is True


def test_mersenne_M61_by_aks_fast():
    assert is_prime_aks_fast(M61) is True


# parallel task will make the caluclation slower here
# because the actual calculation is pow(a, d, n)
# so parallel will not help much here
def test_mersenne_M61_by_miller_rabin_parallel():
    assert is_prime_miller_rabin_parallel(M61) is True


M67 = 2**67 - 1


def test_mersenne_M61_by_trial_division():
    assert is_prime_trial_division(M61) is True


def test_mersenne_M61_by_miller_rabin():
    assert is_prime_miller_rabin(M61) is True
