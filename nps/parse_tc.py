#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import toml
import pprint
from tc_info import PacketInfo

# NOTE
# 나중에 toml 형식이 아닌, 다른 형식의 file format based Tc를 사용 할 수도 있어서,
# 확정성을 위해서 parse_$(lang)_tc(): 라는 이름으로 class를 만듬.
# 만약 json 기반의 tc 파일을 지원한다면 parse_json_tc(): 로 이름을 지어서 파싱을 하면 된다.
# 동일하게, file format의 지원이 끊기거나 nps에서 더이상 지원하지 않을 때는 간단하게


class ParseTomlTc(object):

    def __init__(self):
        print("TOML TC!")

    # Main method, entry point
    def parse_processor(self, file_path, tc_info_list, client_pkt_list, server_pkt_list):
        tc_dict = self.convert_to_dict(file_path)

        # for debugging
        pp = pprint.PrettyPrinter(indent=4)

        # Basic concept for root, sub, element stuff
        # root
        #   - sub
        #       - element
        #   - sub
        #       - element
        for root_tag in tc_dict:
            print(root_tag)
            if root_tag == "TC-information":
                parse_tc_info_node(tc_dict, tc_info_list)

            elif root_tag == "pre-template":
                print("")
                # pp.pprint(tc_dict[root_tag])
            elif root_tag == "post-template":
                print("")
                # pp.pprint(tc_dict[root_tag])

            elif root_tag == "client":
                print("")
                # pp.pprint(tc_dict[root_tag])
                parse_client_tc_info_node(tc_dict, client_pkt_list)
            elif root_tag == "server":
                print("")
                # pp.pprint(tc_dict[root_tag])
                for sub_tag in tc_dict[root_tag]:
                    if sub_tag == "interface":
                        server_pkt_list.set_interface_name(tc_dict[root_tag][sub_tag])
                    elif sub_tag == "ip":
                        server_pkt_list.set_interface_ip(tc_dict[root_tag][sub_tag])
                    elif sub_tag == "port":
                        server_pkt_list.set_interface_port(tc_dict[root_tag][sub_tag])
                    elif sub_tag == "packet":
                        for idx in range(len(tc_dict[root_tag][sub_tag])):
                            pkt_obj = PacketInfo()
                            server_pkt_list.add_pkt_to_list(pkt_obj)

                            for element in tc_dict[root_tag][sub_tag][idx]:
                                if element == "action":
                                    pkt_obj.set_pkt_action(tc_dict[root_tag][sub_tag][idx][element])
                                elif element == "seq":
                                    pkt_obj.set_pkt_seq(tc_dict[root_tag][sub_tag][idx][element])
                                elif element == "ack":
                                    pkt_obj.set_pkt_ack(tc_dict[root_tag][sub_tag][idx][element])
                                elif element == "flags":
                                    pkt_obj.set_pkt_flags(tc_dict[root_tag][sub_tag][idx][element])
                                elif element == "win":
                                    pkt_obj.set_pkt_win(tc_dict[root_tag][sub_tag][idx][element])
                                elif element == "checksum":
                                    pkt_obj.set_pkt_checksum(tc_dict[root_tag][sub_tag][idx][element])
                                elif element == "urg_ptr":
                                    pkt_obj.set_pkt_urg_ptr(tc_dict[root_tag][sub_tag][idx][element])
                                elif element == "len":
                                    pkt_obj.set_pkt_data_len(tc_dict[root_tag][sub_tag][idx][element])
                                elif element == "option":
                                    for option in tc_dict[root_tag][sub_tag][idx][element]:
                                        if option == "mss":
                                            pkt_obj.set_pkt_opt_mss(tc_dict[root_tag][sub_tag][idx][element][option])
                                        elif option == "sack_perm":
                                            pkt_obj.set_pkt_opt_sack_perm(tc_dict[root_tag][sub_tag][idx][element][option])
                                        elif option == "window_scale":
                                            pkt_obj.set_pkt_opt_win_scale(tc_dict[root_tag][sub_tag][idx][element][option])

            else:
                print("TC's containing non-support tags")
                exit(0)

    def convert_to_dict(self, file_path):
        tc_dict = toml.load(file_path)
        # print(tc_dict)

        return tc_dict


def parse_tc_info_node(dict, tc_info_list):
    for sub_tag in dict["TC-information"]:
        if sub_tag == "name":
            tc_info_list.set_tc_info_name(dict["TC-information"][sub_tag])
        elif sub_tag == "options":
            for element in dict["TC-information"][sub_tag]:
                if element == "use_auto_seq":
                    tc_info_list.set_tc_info_auto_seq(dict["TC-information"][sub_tag][element])
                elif element == "use_fixed_win_size":
                    tc_info_list.set_tc_info_fixed_win(dict["TC-information"][sub_tag][element])

def parse_pkt_list_info_node(dict, pkt_list, dir):
    for sub_tag in dict["client"]:
        if sub_tag == "interface":
            pkt_list.set_interface_name(dict[root_tag][sub_tag])
        elif sub_tag == "ip":
            pkt_list.set_interface_ip(dict[root_tag][sub_tag])
        elif sub_tag == "port":
            pkt_list.set_interface_port(dict[root_tag][sub_tag])
        elif sub_tag == "packet":
            for idx in range(len(dict[root_tag][sub_tag])):
                pkt_obj = PacketInfo()
                client_pkt_list.add_pkt_to_list(pkt_obj)

                for element in dict[root_tag][sub_tag][idx]:
                    if element == "action":
                        pkt_obj.set_pkt_action(dict[root_tag][sub_tag][idx][element])
                    elif element == "seq":
                        pkt_obj.set_pkt_seq(dict[root_tag][sub_tag][idx][element])
                    elif element == "ack":
                        pkt_obj.set_pkt_ack(dict[root_tag][sub_tag][idx][element])
                    elif element == "flags":
                        pkt_obj.set_pkt_flags(dict[root_tag][sub_tag][idx][element])
                    elif element == "win":
                        pkt_obj.set_pkt_win(dict[root_tag][sub_tag][idx][element])
                    elif element == "checksum":
                        pkt_obj.set_pkt_checksum(dict[root_tag][sub_tag][idx][element])
                    elif element == "urg_ptr":
                        pkt_obj.set_pkt_urg_ptr(dict[root_tag][sub_tag][idx][element])
                    elif element == "len":
                        pkt_obj.set_pkt_data_len(dict[root_tag][sub_tag][idx][element])
                    elif element == "option":
                        for option in dict[root_tag][sub_tag][idx][element]:
                            if option == "mss":
                                pkt_obj.set_pkt_opt_mss(dict[root_tag][sub_tag][idx][element][option])
                            elif option == "sack_perm":
                                pkt_obj.set_pkt_opt_sack_perm(dict[root_tag][sub_tag][idx][element][option])
                            elif option == "window_scale":
                                pkt_obj.set_pkt_opt_win_scale(dict[root_tag][sub_tag][idx][element][option])




class ParseJsonTc(object):

    def __init__(self):
        print("TBS")

    # Main method, entry point
    def parse_prosessor(self, file_path):
        print("TBS")

    def convert_to_dict(self, file_path):
        print("TBS")
