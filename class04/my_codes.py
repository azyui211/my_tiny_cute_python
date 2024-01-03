# -*- coding:utf-8 -*-

import os

def make_dirs(file_path):
    if os.path.isfile(file_path):
        dir_path = os.path.dirname(file_path)
    else:
        dir_path = file_path
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
