import argparse
from src.trial_division import is_prime as is_prime_trial_division
from src.fermat import is_prime as is_prime_fermat
from src.miller_rabin import is_prime as is_prime_miller_rabin
from src.aks import is_prime as is_prime_aks

# Map algorithm names (used on the command line) to their implementations
ALGORITHMS = {
    # full name
    "trial": is_prime_trial_division,
    "fermat": is_prime_fermat,
    "miller_rabin": is_prime_miller_rabin,
    "aks": is_prime_aks,
    # short name
    "t": is_prime_trial_division,
    "f": is_prime_fermat,
    "m": is_prime_miller_rabin,
    "a": is_prime_aks,
}


def main():
    #  command line arguments handling
    parser = argparse.ArgumentParser(description="Check whether a number is prime.")
    parser.add_argument("number", type=int, help="The integer to test for primality.")
    parser.add_argument(
        "-a",
        "--algorithm",
        choices=ALGORITHMS.keys(),
        default="trial",
        help="Primality test algorithm to use (default: trial).",
    )
    args = parser.parse_args()

    validate_prime = ALGORITHMS[args.algorithm]
    result = validate_prime(args.number)
    print(f"{args.algorithm}: {args.number} is {'prime' if result else 'not prime'}")


if __name__ == "__main__":
    main()
