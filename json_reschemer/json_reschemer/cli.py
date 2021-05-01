"""Console script for json_reschemer."""
import argparse
import sys

def parse_my_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('_', nargs='*') # Any extra cheeseburgers
    parser.add_argument('--foo', help="the foo param, duh")
    parser.add_argument('--bar', help="its the bar param, come on")
    args = parser.parse_args()

    print("ARGS: {}".format(args))
    return args

def run():
    return parse_my_args()

if __name__ == "__main__":
    run()
    sys.exit()  # pragma: no cover
