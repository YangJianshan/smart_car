# !/usr/bin/python3
# coding=utf-8

from app import app
from views import *
from api import *


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5515)
