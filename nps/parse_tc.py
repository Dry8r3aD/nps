#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import toml
import pprint

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
                pp.pprint(tc_dict[root_tag])
                for sub_tag in tc_dict[root_tag]:
                    if sub_tag == "name":
                        tc_info_list.tc_name = tc_dict[root_tag][sub_tag]
                        # pp.pprint(tc_dict[root_tag][sub_tag])
                    elif sub_tag == "options":
                        print("options")
                        for element in tc_dict[root_tag][sub_tag]:
                            if element == "use_auto_seq":
                                print("dd")
                                tc_info_list.tc_opt_auto_seq = tc_dict[root_tag][sub_tag][element]
                                pp.pprint(tc_dict[root_tag][sub_tag])
                            elif element == "use_fixed_win_size":
                                print("ee")
                                tc_info_list.tc_opt_fixed_win = tc_dict[root_tag][sub_tag][element]
                                pp.pprint(tc_dict[root_tag][sub_tag])

            elif root_tag == "pre-template":
                pp.pprint(tc_dict[root_tag])
            elif root_tag == "post-template":
                pp.pprint(tc_dict[root_tag])
            elif root_tag == "client":
                pp.pprint(tc_dict[root_tag])
            elif root_tag == "server":
                pp.pprint(tc_dict[root_tag])
            else:
                print("TC's containing non-support tags")
                exit(0)



    def convert_to_dict(self, file_path):
        tc_dict = toml.load(file_path)
        print(tc_dict)

        return tc_dict

        #
        # parse_tc_data()
        #
        # # spliting & parsing root tags
        #


class ParseJsonTc(object):

    def __init__(self):
        print("TBS")

    # Main method, entry point
    def parse_prosessor(self, file_path):
        print("TBS")

    def convert_to_dict(self, file_path):
        print("TBS")
