import argparse
import sys

def main():
    parser = argparse.ArgumentParser(
        description="Generate transaction data to deploy any random hex string to Ethereum"
    )

    inputs = parser.add_argument_group("input arguments")
    inputs.add_argument(
        "-b",
        "--bytecode",
        help="hex-encoded bytecode string (60606040...)"
    )
    args = parser.parse_args()

    if not (
        args.bytecode
    ):
        parser.print_help()
        sys.exit(0)

if __name__ == "__main__":
    main()
