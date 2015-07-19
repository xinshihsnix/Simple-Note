# -*- coding:utf-8 -*-
import pickle
import os.path
import settings

class Messager:
    def __init__(self, file_path=settings.DATA_STORED_PATH, *args, **kwargs):
        self.file_path = file_path
        self._file = None
        self.data_source = None

    def data_exist(self):
        return os.path.exists(self.file_path)

    def activate_data_source(self, type='r'):
        """
        param: type ('r': read, 'w': write)
        return: Boolean
        """
        if self.data_exist():
            if type == 'r':
                self._file = open(self.file_path, 'rb')
                self.data_source = pickle.load(self._file)
                self.company_data = self.data_source.get(settings.COMPANY)
            elif type == 'w':
                self._file = open(self.file_path, 'wb')


    def persistence_data_source(self):
        """
        持久化数据
        """
        pickle.dump(self.data_source, self._file, -1)
        self.file_close()

    def file_close(self):
        if self._file:
            self._file.close()

    def get_info_by_key(self, key):
        print 'xxx'
        print self.company_data.get(key)

    def get_info_grep(self):
        pass

    def set_info(self, key, value):
        # key = str(key)
        # value = str(value)
        self.activate_data_source(type='w')
        self.company_data.update({key: value})
        self.persistence_data_source()

