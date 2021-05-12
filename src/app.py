# !/usr/bin/python3
# coding=utf-8

from flask import Flask
from config import DebugConfig

app = Flask(__name__, static_url_path='')
app.config.from_object(DebugConfig)
