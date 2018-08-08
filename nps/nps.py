#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import sys
from parse_tc import *
from tc_info import TestCaseInfo, PacketList


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", help="TC File name", required=True)
    parser.add_argument("-t", "--format", help="TC File format. Default TOML")
    parser.add_argument("-v", "--verbose", help="Verbose mode, enables detail log")
    parser.add_argument("-l", "--log", help="Log file's path")
    args = parser.parse_args()

    # If the arg's count is less then 1
    if len(sys.argv) <= 1:
        parser.print_help()
        exit(0)

    # If TC Filename is not entered
    if args.file is None:
        print("TC File is not defined!")
        exit(0)

    # TC File format
    if args.format is None:
        print("TC File format is not given, set to default format : TOML")
        tc_format = "toml"
    else:
        tc_format = args.format.lower()

    # Class 생성
    tc_info_list = TestCaseInfo()
    client_pkt_list = PacketList("client")
    server_pkt_list = PacketList("server")

    # tc_analyzer is different per TC File format
    # nps only supports "TOML" for now
    if tc_format == "toml":
        tc_analyzer = ParseTomlTc()
    elif tc_format == "json":
        tc_analyzer = ParseJsonTc()
    else:
        print("Unsupported TC file format")
        exit(0)

    # Parse TC's content and assign it to the classes created above
    tc_analyzer.parse_processor(args.file, tc_info_list, client_pkt_list, server_pkt_list)

    print(tc_info_list.tc_name + "&&&" + tc_info_list.tc_opt_auto_seq + "$$$$" + tc_info_list.tc_opt_fixed_win)

if __name__ == "__main__":
    exit(main())
