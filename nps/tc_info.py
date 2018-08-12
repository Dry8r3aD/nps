#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import netifaces


# TestCaseInfo
#
# 실행 할 TC( Test Case )의 info를 저장한다.
# 저장하는 TC 정보의 예시로 auto seq / ack 기능, using fixed window size 기능 등이 있다.
class TestCaseInfo(object):
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


# PacketList
#
# 한개의 TC 파일당 Client / Server 각 한개씩, 총 두개의 PacketList가 생성된다.
# PacketList class는 안에 Packet
class PacketList(object):

    # Initialize
    def __init__(self, name):
        print("New Packet List created : " + name)

        # Variables                     # Explanation : Example( Format )
        self.packet_list_name = name    # name
        self.interface_name = ""        # Interface name : tp0, eth0, opt0
        self.interface_mac = ""         # Interface MAC address : 12:34:56:ab:cd:ef
        self.interface_ip = ""          # Interface IP address : 192.168.0.1, 1.1.1.1
        self.interface_port = 0         # Interface port : 1 ~ 65535

        self.pkt_list = []
        self.pkt_list.clear()           # Packet list : List PacketInfo objects

    def set_interface_name(self, name):
        self.interface_name = name
        self.set_interface_mac(name)

    def set_interface_mac(self, name):
        self.interface_mac = netifaces.ifaddresses(name)[netifaces.AF_LINK][0]['addr']

    def set_interface_ip(self, ip):
        self.interface_ip = ip

    def set_interface_port(self, port):
        self.interface_port = port

    def add_pkt_to_list(self, pkt):
        self.pkt_list.append(pkt)


# PacketInfo
#
# 한개의 패킷에 대한 객체
class PacketInfo(object):

    # Initialize
    def __init__(self):
        print("New Packet obj created")

        # Variables             # Explanation : Example( Format )
        # General Packet Information Variables
        self.pkt_action = ""         # Packet action : send, recv, wait

        # TCP Header Variables
        self.pkt_flags = []          # TCP flags( Multi-select possible ) : syn, ack, fin, rst
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

    def set_pkt_action(self, action):
        self.pkt_action = action

    def set_pkt_flags(self, flags):
        self.pkt_flags.append(flags)

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


