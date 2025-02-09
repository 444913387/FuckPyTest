# -*- coding: utf-8 -*-
__author__ = 'WangJianyu'
__date__ = '2018/2/14'

import logging
import os
from logging.handlers import TimedRotatingFileHandler

# 日志级别
CRITICAL = 50
FATAL = CRITICAL
ERROR = 40
WARNING = 30
WARN = WARNING
INFO = 20
DEBUG = 10
NOTSET = 0

CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))
ROOT_PATH = os.path.join(CURRENT_PATH, os.pardir)
# print(os.pardir)
LOG_PATH = '../logs/'
# print(LOG_PATH)

# 如果没有这个log文件 就创建一个
if not os.path.exists(LOG_PATH):
    os.mkdir(LOG_PATH)


class LogMan(logging.Logger):

    def __init__(self, name, level=INFO, stream=True, file=True):
        self.name = name
        self.level = level
        logging.Logger.__init__(self, self.name, level=level)
        self.file_handler = None
        if stream:

            self.set_stream_handler()
        if file:

            self.set_file_handler()

    def set_stream_handler(self, level=None):
        file_name = os.path.join(LOG_PATH, '{name}.log'.format(name=self.name))
        # 设置日志回滚, 保存在log目录, 一天保存一个文件, 保留1年 365天
        file_handler = TimedRotatingFileHandler(filename=file_name, when='D', interval=1, backupCount=365,
                                                encoding='utf-8')
        file_handler.suffix = '%Y%m%d.log'
        if not level:
            file_handler.setLevel(self.level)
        else:
            file_handler.setLevel(level)
        formatter = logging.Formatter(
            '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
        file_handler.setFormatter(formatter)
        self.file_handler = file_handler
        self.addHandler(file_handler)

    def set_file_handler(self, level=None):
        stream_handler = logging.StreamHandler()
        formatter = logging.Formatter(
            '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
        stream_handler.setFormatter(formatter)
        if level is None:
            stream_handler.setLevel(self.level)
        else:
            stream_handler.setLevel(level)
        self.addHandler(stream_handler)

    def reset_name(self, name):
        self.name = name
        self.removeHandler(self.file_handler)
        self.set_file_handler()
