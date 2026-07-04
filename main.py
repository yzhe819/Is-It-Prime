import argparse
from src.trial_division import is_prime as is_prime_trial_division
from src.fermat import is_prime as is_prime_fermat
from src.miller_rabin import is_prime as is_prime_miller_rabin
from src.aks import is_prime as is_prime_aks
from src.aks_numpy import is_prime as is_prime_aks_numpy

# Map algorithm names (used on the command line) to their implementations
ALGORITHMS = {
    # full name
    "trial": is_prime_trial_division,
    "fermat": is_prime_fermat,
    "miller_rabin": is_prime_miller_rabin,
    "aks": is_prime_aks,
    "aks_numpy": is_prime_aks_numpy,
    "aks_fft": is_prime_aks_fft,
    "aks_fast": is_prime_aks_fast,

    # short name
    "t": is_prime_trial_division,
    "f": is_prime_fermat,
    "m": is_prime_miller_rabin,
    "a": is_prime_aks,
    "an": is_prime_aks_numpy,
    "af": is_prime_aks_fft,
}


def main():
    #  command line arguments handling
    parser = argparse.ArgumentParser(description="Check whether a number is prime.")
    parser.add_argument("number", type=int, help="The integer to test for primality.")
    parser.add_argument(
        "-a",
        "--algorithm",
        choices=ALGORITHMS.keys(),
        default="miller_rabin", # default to miller-rabin because it is fast and reliable
        help="Primality test algorithm to use (default: trial).",
    )
    args = parser.parse_args()

    validate_prime = ALGORITHMS[args.algorithm]
    result = validate_prime(args.number)
    print(f"{args.algorithm}: {args.number} is {'prime' if result else 'not prime'}")


if __name__ == "__main__":
    main()
