# -*- coding:utf-8 -*-
import pickle
import os.path

class Messager:
    def __init__(self, file_path, command, content):
        self.file_path = file_path
        self.command = command
        self.content = content
        self.data_source = None

    def data_exist(self):
        return os.path.exists(self.file_path)

    def get_read_data(self):
        if self.data_exist():
            f = open(self.file_path, 'rb')
            self.data_source = pickle.load(f)

    def get_write_data(self):
        if self.data_exist():
            f = open(self.file_path, 'wb')
            self.data_source = pickle.load(f)

    def close_data_source(self):
        if self.data_source:
            self.data_source.close()

