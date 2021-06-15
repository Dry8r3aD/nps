#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from parse_tc import *
from tc_info import TestCaseInfo, PacketObjList
from scapy.all import *
import argparse
import sys
import pprint
import scapy


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
    pkt_list = PacketObjList("Packet List")

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
    tc_analyzer.parse_processor(args.file, tc_info_list, pkt_list)

    # client pkt_list processor / server pkt_list processor
    # Read pkt_list -> create pkt -> rx / tx / wait

    # print(tc_info_list.tc_name + "&&&" + tc_info_list.tc_opt_auto_seq + "$$$$" + tc_info_list.tc_opt_fixed_win)
    # print(client_pkt_list.interface_mac)
    # print(client_pkt_list.interface_name + "  " + server_pkt_list.interface_name)

    print(tc_info_list)
    print(pkt_list)

    for pkt_obj in pkt_list.pkt_list:
        resp = sr(pkt_obj.pkt, timeout=2)
        print(resp)
        


if __name__ == "__main__":
    exit(main())
