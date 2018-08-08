#!/usr/bin/env python
# -*- coding: UTF-8 -*-


# TestCaseInfo
#
# 실행 할 TC( Test Case )의 info를 저장한다.
# 저장하는 TC 정보의 예시로 auto seq / ack 기능, using fixed window size 기능 등이 있다.
class TestCaseInfo(object):

    # Developer's commend
    # => TO BE ERASED BEFORE COMMIT
    # feature 사용 여부를 on/off, enable/disable, true/false 등 어떤걸 사용하는게 좋을까?

    # Variables             # Explanation : Example( Format )
    tc_name = ""            # TC name : tcp_connection_open_01
    tc_opt_auto_seq = ""    # TC auto seq/ack filling feature : on, off
    tc_opt_fixed_win = ""   # TC fixed window size feature : on, off

    # Initialize
    def __init__(self):
        print("Hello World~~!")


# PacketList
#
# 한개의 TC 파일당 Client / Server 각 한개씩, 총 두개의 PacketList가 생성된다.
# PacketList class는 안에 Packet
class PacketList(object):

    # Variables             # Explanation : Example( Format )
    packet_list_name = ""   # name

    interface_name = ""     # Interface name : tp0, eth0, opt0
    interface_mac = ""      # Interface MAC address : 12:34:56:ab:cd:ef
    interface_ip = ""       # Interface IP address : 192.168.0.1, 1.1.1.1
    interface_port = 0      # Interface port : 1 ~ 65535

    pkt_list = []           # Packet list : List PacketInfo objects

    # Initialize
    def __init__(self, name):
        print("Hello World!" + name)
        packet_list_name = name


# PacketInfo
#
# 한개의 패킷에 대한 객체
class PacketInfo(object):

    # Variables             # Explanation : Example( Format )
    # General Packet Information Variables
    pkt_action = ""         # Packet action : send, recv, wait

    # TCP Header Variables
    pkt_flags = []          # TCP flags( Multi-select possible ) : syn, ack, fin, rst
    pkt_seq = 0             # Sequence number : 32bit range...
    pkt_ack = 0             # Acknowledge number : 32bit range...
    pkt_win = 0             # Window size : 0 ~ 65535
    pkt_sum = ""            # TCP Checksum : 0x123
    pkt_urg_ptr = 0         # TCP urgent pointer : 0 ~ 65535
    pkt_data_len = 0        # Packet payload length : 1460

    # TCP Header Option Variables
    pkt_opt_mss = 0         # TCP MSS size : 1460
    pkt_opt_sack_perm = ""  # TCP SACK perm : on, off
    pkt_opt_win_scale = 0   # TCP window scale : 0 ~ 256

    # Initialize
    def __init__(self):
        print("Hello World!")



