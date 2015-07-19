import pickle
import os.path
from settings import *

if os.path.exists(DATA_STORED_PATH):
    f = open(DATA_STORED_PATH, 'rb')
    try:
        data = pickle.load(f)
    except Exception, e:
        f.close()
        w_file = open(DATA_STORED_PATH, 'wb')
        input = {
            COMPANY: {}
        }
        pickle.dump(input, w_file, -1)
        w_file.close()
        print '---Exception---init.py:', e
    print data