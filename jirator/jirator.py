from workaction import WorkAction
import argparse

parser = argparse.ArgumentParser(description="Default argument parser")
parser.add_argument("--version", action="version", version="jirator %s" % ("not-specified"), help="show the current jirator version information")
parser.add_argument("work", action=WorkAction, help="select issue from list and checkout to that branch")

def main():
    args = parser.parse_args()

if __name__== '__main__':
    main()
