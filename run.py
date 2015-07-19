# -*- coding:utf-8 -*-
import sys, optparse
from optparse import OptionParser
from messager import Messager

MSG_USAGE = "usage: python %prog [options]"

optParser = OptionParser(MSG_USAGE)

optParser.add_option("-g",
                     "--get",
                     action = "store",
                     type = "string",
                     dest = "key_get")

optParser.add_option("-s",
                     "--set",
                     action = "store",
                     type = "string",
                     dest = "key_set")

options, args = optParser.parse_args(sys.argv)

if options.key_get:
    m = Messager()
    m.get_info_by_key(options.key_get)

if options.key_set:
    key = options.key_set
    value = args[0]
    m = Messager()
    m.set_info(key, value)


