#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import toml
import argparse
import sys
from parse_tc import parse_toml_tc
from tc_info import packet_info


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", help="TC File name", required="true")
    parser.add_argument("-v", "--verbose", help="Verbose mode, enables detail log")
    parser.add_argument("-l", "--log", help="Log file's path")
    args = parser.parse_args()

    # If the arg's count is less then 1
    if len(sys.argv) <= 1:
        parser.print_help()
        exit(0)

    # If TC Filename is not entered
    if args.file == None:
        print("TC File is not defined!")
        exit(0)

    # Parse the toml tc file to dictionary
    tc_conventer = parse_toml_tc()
    tc_conventer.convert_toml_to_dic(args.file)


if __name__ == "__main__":
    exit(main())

