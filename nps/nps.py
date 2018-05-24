#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import sys

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", help="TC File name", required="true")
    args = parser.parse_args()

    # If the arg's count is less then 1
    if len(sys.argv) <= 1:
        parser.print_help()
        exit(0)

    # If TC Filename is not entered
    if args.file == None:
        print("TC File is not defined!")
        exit(0)

    print(args.file)


if __name__ == "__main__":
    exit(main())

