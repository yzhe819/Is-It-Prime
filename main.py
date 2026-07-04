import argparse
from src.trial_division import is_prime as is_prime_trial_division

# Map algorithm names (used on the command line) to their implementations
ALGORITHMS = {
    "trial": is_prime_trial_division,
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
