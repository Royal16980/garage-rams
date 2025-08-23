"""Command line interface for the risk assessment app."""

import argparse
from .core import risk_level


def main(argv=None):
    parser = argparse.ArgumentParser(description="Compute risk level")
    parser.add_argument("--probability", type=float, required=True, help="Probability between 0 and 1")
    parser.add_argument("--impact", type=float, required=True, help="Impact between 0 and 1")
    args = parser.parse_args(argv)

    level = risk_level(args.probability, args.impact)
    print(f"Risk level: {level}")


if __name__ == "__main__":
    main()
