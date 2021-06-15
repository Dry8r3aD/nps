#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import netifaces
from scapy.all import *


# TestCaseInfo
#
# 실행 할 TC( Test Case )의 info를 저장한다.
# 저장하는 TC 정보의 예시로 auto seq / ack 기능, using fixed window size 기능 등이 있다.
class TestCaseInfo:
    # Developer's commend
    # => TO BE ERASED BEFORE COMMIT
    # feature 사용 여부를 on/off, enable/disable, true/false 등 어떤걸 사용하는게 좋을까?

    # Initialize
    def __init__(self):
        print("New TC Info obj created")

        # Variables                     # Explanation : Example( Format )
        self.tc_name = ""               # TC name : tcp_connection_open_01
        self.tc_opt_auto_seq = ""       # TC auto seq/ack filling feature : on, off
        self.tc_opt_fixed_win = ""      # TC fixed window size feature : on, off

    def set_tc_info_name(self, name):
        self.tc_name = name

    def set_tc_info_auto_seq(self, flag):
        self.tc_opt_auto_seq = flag

    def set_tc_info_fixed_win(self, flag):
        self.tc_opt_fixed_win = flag


# PacketObjList
class PacketObjList:

    # Initialize
    def __init__(self, name) -> None:
        print("New Packet List created : " + name)

        # Variables                     # Explanation : Example( Format )
        self.packet_list_name = name    # name
        self.interface_name = ""        # Interface name : tp0, eth0, opt0
        self.interface_mac = ""         # Interface MAC address : 12:34:56:ab:cd:ef
        self.src_ip = ""                # Source IP address : 192.168.0.1, 1.1.1.1
        self.src_port = 0               # Source IP Port

        self.dst_ip = ""            
        self.dst_port = 0               

        self.pkt_list = []
        self.pkt_list.clear()           # Packet list : List PacketInfo objects

    def __str__(self) -> str:
        for pkt in self.pkt_list:
            print(pkt)
        
        return self.packet_list_name

    def set_interface_name(self, name) -> None:
        self.interface_name = name
        self.set_interface_mac(name)

    def get_interface_name(self) -> str:
        return self.interface_name

    def set_interface_mac(self, name):
        self.interface_mac = netifaces.ifaddresses(name)[netifaces.AF_LINK][0]['addr']

    def get_interface_mac(self) -> str:
        return self.interface_mac

    def set_src_ip(self, ip):
        self.src_ip = ip

    def get_src_ip(self) -> str:
        return self.src_ip

    def set_dst_ip(self, ip):
        self.dst_ip = ip

    def get_dst_ip(self) -> str:
        return self.dst_ip

    def set_src_port(self, port):
        self.src_port = port

    def get_src_port(self) -> int:
        return self.src_port

    def set_dst_port(self, port):
        self.dst_port = port
    
    def get_dst_port(self) -> int:
        return self.dst_port

    def add_pkt_to_list(self, pkt):
        self.pkt_list.append(pkt)


# PacketInfo
#
# 한개의 패킷에 대한 객체
class PacketInfo:

    # Initialize
    def __init__(self, interface, src_ip, dst_ip, src_port, dst_port):
        print("New Packet obj created")

        # Variables             # Explanation : Example( Format )
        # General Packet Information Variables
        self.pkt_action = ""         # Packet action : send, recv, wait

        # TCP Header Variables
        self.pkt_flags = list()      # TCP flags( Multi-select possible ) : syn, ack, fin, rst
        self.pkt_seq = 0             # Sequence number : 32bit range...
        self.pkt_ack = 0             # Acknowledge number : 32bit range...
        self.pkt_win = 0             # Window size : 0 ~ 65535
        self.pkt_sum = ""            # TCP Checksum : 0x123
        self.pkt_urg_ptr = 0         # TCP urgent pointer : 0 ~ 65535
        self.pkt_data_len = 0        # Packet payload length : 1460

        # TCP Header Option Variables
        self.pkt_opt_mss = 0         # TCP MSS size : 1460
        self.pkt_opt_sack_perm = ""  # TCP SACK perm : on, off
        self.pkt_opt_win_scale = 0   # TCP window scale : 0 ~ 256

        # Data (Content)
        self. data = ""

        # Actual Packet Data
        self.pkt = IP(src=src_ip, dst=dst_ip) / TCP(sport=src_port, dport=dst_port)

    def __str__(self) -> str:
        return "Action: {} // Flag: {} // Seq: {} // Ack: {}".format(
            self.pkt_action, self.pkt_flags, self.pkt_seq, self.pkt_ack
        )

    def convert_tcp_flags(self):
        if "SYN" and "ACK" in self.pkt_flags:
            return "SA"
        elif "FIN" and "ACK" in self.pkt_flags:
            return "FA"
        elif "SYN" in self.pkt_flags:
            return "S"
        elif "FIN" in self.pkt_flags:
            return "F"
        elif "RST" in self.pkt_flags:
            return "R"
        elif "ACK" in self.pkt_flags:
            return "A"
        else:
            print("Not supported TCP Flag detected ({})".format(self.pkt_flags))
            return "N/A"

    def get_tcp_options(self) -> list():
        options = list()
        
        if "SYN" in self.pkt_flags:
            if self.pkt_opt_mss:
                options.append(("MSS", self.pkt_opt_mss))
            if self.pkt_opt_win_scale:
                options.append(("WScale", self.pkt_opt_win_scale))
            if self.pkt_opt_sack_perm:
                options.append(("SAckOK", self.pkt_opt_sack_perm))

        return options

    def create_pkt(self):
        tcp = self.pkt[TCP]
        ip = self.pkt[IP]
        data = self.data

        tcp.seq = self.pkt_seq
        tcp.ack = self.pkt_ack
        tcp.flags = self.convert_tcp_flags()
        tcp.options = self.get_tcp_options()

        self.pkt = ip / tcp / data
        self.pkt.display()

    def set_pkt_action(self, action):
        self.pkt_action = action

    def set_pkt_flags(self, flags):
        self.pkt_flags = flags

    def set_pkt_seq(self, seq):
        self.pkt_seq = seq

    def set_pkt_ack(self, ack):
        self.pkt_ack = ack

    def set_pkt_win(self, win):
        self.pkt_win = win

    def set_pkt_checksum(self, sum):
        self.pkt_sum = sum

    def set_pkt_urg_ptr(self, urg):
        self.pkt_urg_ptr = urg

    def set_pkt_data_len(self, len):
        self.pkt_data_len = len

    def set_pkt_opt_mss(self, mss):
        self.pkt_opt_mss = mss

    def set_pkt_opt_sack_perm(self, perm):
        self.pkt_opt_sack_perm = perm

    def set_pkt_opt_win_scale(self, scale):
        self.pkt_opt_win_scale = scale


