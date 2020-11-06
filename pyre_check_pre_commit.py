#!/usr/bin/env python3

import argparse
import os

EXE = "pyre"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--work-dir", dest="work_dir")

    args, unknown = parser.parse_known_args()

    unknown.insert(0, EXE)
    if args.work_dir:
        os.chdir(args.work_dir)
    os.execvp(EXE, args=unknown)


if __name__ == "__main__":
    main()
