# !/usr/bin/python3
# coding=utf-8

import abc


class Config(metaclass=abc.ABCMeta):
    DEBUG = False
    static_url_path = ''
    pass


class DebugConfig(Config):
    DEBUG = True
    TESTING = True
    pass
