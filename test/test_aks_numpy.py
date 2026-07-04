import pytest
from src.aks_numpy import is_prime

# Primes under 1000
PRIMES_UNDER_1000 = [
    2,
    3,
    5,
    7,
    11,
    13,
    17,
    19,
    23,
    29,
    31,
    37,
    41,
    43,
    47,
    53,
    59,
    61,
    67,
    71,
    73,
    79,
    83,
    89,
    97,
    101,
    103,
    107,
    109,
    113,
    127,
    131,
    137,
    139,
    149,
    151,
    157,
    163,
    167,
    173,
    179,
    181,
    191,
    193,
    197,
    199,
    211,
    223,
    227,
    229,
    233,
    239,
    241,
    251,
    257,
    263,
    269,
    271,
    277,
    281,
    283,
    293,
    307,
    311,
    313,
    317,
    331,
    337,
    347,
    349,
    353,
    359,
    367,
    373,
    379,
    383,
    389,
    397,
    401,
    409,
    419,
    421,
    431,
    433,
    439,
    443,
    449,
    457,
    461,
    463,
    467,
    479,
    487,
    491,
    499,
    503,
    509,
    521,
    523,
    541,
    547,
    557,
    563,
    569,
    571,
    577,
    587,
    593,
    599,
    601,
    607,
    613,
    617,
    619,
    631,
    641,
    643,
    647,
    653,
    659,
    661,
    673,
    677,
    683,
    691,
    701,
    709,
    719,
    727,
    733,
    739,
    743,
    751,
    757,
    761,
    769,
    773,
    787,
    797,
    809,
    811,
    821,
    823,
    827,
    829,
    839,
    853,
    857,
    859,
    863,
    877,
    881,
    883,
    887,
    907,
    911,
    919,
    929,
    937,
    941,
    947,
    953,
    967,
    971,
    977,
    983,
    991,
    997,
]


@pytest.mark.parametrize("p", PRIMES_UNDER_1000)
def test_primes_under_1000(p):
    assert is_prime(p) is True


# Composite number tests
COMPOSITE_NUMBERS = [
    4,
    6,
    8,
    9,
    10,
    12,
    15,
    16,
    21,
    25,
    27,
    33,
    49,
    51,
    77,
    91,
    100,
    121,
    169,
    200,
    221,
    289,
    361,
    500,
    529,
    841,
    961,
    998,
]


@pytest.mark.parametrize("c", COMPOSITE_NUMBERS)
def test_composite_numbers(c):
    assert is_prime(c) is False


# Carmichael numbers -- composites that fool the Fermat primality test
# (they satisfy a^(n-1) = 1 mod n for almost every base a).
CARMICHAEL_NUMBERS = [
    561,  # 3 × 11 × 17   (smallest Carmichael number)
    1105,  # 5 × 13 × 17
    1729,  # 7 × 13 × 19   (the famous "taxicab number")
    2465,  # 5 × 17 × 29
    2821,  # 7 × 13 × 31
    6601,  # 7 × 23 × 41
    8911,  # 7 × 19 × 67
    10585,  # 5 × 29 × 73
    15841,  # 7 × 31 × 73
    29341,  # 13 × 37 × 61
]


@pytest.mark.parametrize("n", CARMICHAEL_NUMBERS)
def test_carmichael_numbers_are_composite(n):
    assert is_prime(n) is False


# Edge cases (worth covering -- common source of off-by-one errors)
@pytest.mark.parametrize(
    "n,expected",
    [
        (0, False),
        (1, False),
        (2, True),  # smallest prime
        (3, True),
    ],
)
def test_edge_cases(n, expected):
    assert is_prime(n) is expected
