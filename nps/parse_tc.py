#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import toml
import pprint


class parse_toml_tc():

    def convert_toml_to_dic( self, file_path):

        tc_dic = toml.load( file_path )

        print(tc_dic)

        parse_tc_data()

        # spliting & parsing root tags

        pp = pprint.PrettyPrinter(indent=4)

        for root_tag in tc_dic:
            print(root_tag)
            if root_tag == "TC-information":
                pp.pprint(tc_dic[root_tag])
            elif root_tag == "template":
                pp.pprint(tc_dic[root_tag])
            elif root_tag == "client":
                pp.pprint(tc_dic[root_tag])
            elif root_tag == "server":
                pp.pprint(tc_dic[root_tag])
            else:
                print("TC's containing non-support tags")
                exit(0)

