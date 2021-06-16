#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from parse_tc import *
from tc_info import TestCaseInfo, PacketObjList
from scapy.all import *
import logging
import argparse
import sys
import pprint


def compare_pkts(original, target) -> bool:
    # DO NOT Validate 5-Tuple Information
    # We use sr and sr1 for the packet receiving, which only returns 
    # a answer packet from the testing session.
    # Since "session" is guaranteed, we don'y need to check the 5 information,
    # protocol, src/dst IP address, and src/dst port number.

    # DEBUG Logging
    if logging.root.level == logging.DEBUG:
        target.display()

    if original.pkt_seq and original.pkt_seq != target[TCP].seq:
        logging.debug("COMPARE FAILED (Sequence)")
        return False
    
    if original.pkt_ack and original.pkt_ack != target[TCP].ack:
        logging.debug("COMPARE FAILED (Acknowledgement)")
        return False

    if original.pkt_flags and original.convert_tcp_flags() != target[TCP].flags:
        logging.debug("COMPARE FAILED (Flags)")
        return False

    if original.pkt_win and original.pkt_win != target[TCP].window:
        logging.debug("COMPARE FAILED (Window Size - W/o Scale applied)")
        return False
    
    if original.pkt_sum and original.pkt_sum != target[TCP].chksum:
        logging.debug("COMPARE FAILED (Checksum)")
        return False

    return True


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", help="TC File name", required=True)
    parser.add_argument("-t", "--format", help="TC File format. Default TOML")
    parser.add_argument("-v", "--verbose", action='store_true', help="Verbose mode, enables detail log")
    parser.add_argument("-l", "--log", help="Log file's path")
    args = parser.parse_args()

    # If the arg's count is less then 1
    if len(sys.argv) <= 1:
        parser.print_help()
        exit(0)

    # If TC Filename is not entered
    if args.file is None:
        logging.error("TC File is not defined!")
        exit(0)

    # Logggin Verbose Mode
    if args.verbose:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)

    # TC File format
    if args.format is None:
        logging.info("TC File format is not given, set to default format : TOML")
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
        logging.error("Unsupported TC file format")
        exit(0)

    # Parse TC's content and assign it to the classes created above
    tc_analyzer.parse_processor(args.file, tc_info_list, pkt_list)

    # Send & Recv
    for pkt_obj in pkt_list.pkt_list:
        if logging.root.level == logging.DEBUG:
            pkt_obj.pkt.display()

        if pkt_obj.get_pkt_action() == "SEND":
            resp = sr1(pkt_obj.pkt)
            continue

        if compare_pkts(pkt_obj, resp) is not True:
            logging.info("TC Failed!")
            exit(0)

    logging.info("TC Success!")

        
if __name__ == "__main__":
    exit(main())
