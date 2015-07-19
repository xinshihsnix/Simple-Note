# -*- coding:utf-8 -*-
import pickle
import os
from settings import *


"""
若文件不存在：创建并初始化
若文件内格式不正确：初始化
"""
try:
    f = open(DATA_STORED_PATH, 'rb')
    pickle.load(f)
    f.close()
except Exception, e:
    w_file = open(DATA_STORED_PATH, 'wb')
    input = {
        COMPANY: {}
    }
    pickle.dump(input, w_file, -1)

    w_file.close()
    print '---Exception:', e, u'已被处理'
