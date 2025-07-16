import argparse
parser = argparse.ArgumentParser(description="Check if any arguments are passed.")
parser.add_argument("args", nargs="*", help="Arguments to check")
args = parser.parse_args()
if args.args:
    print("Arguments passed:", args.args)
else:
    print("No arguments Passed")
