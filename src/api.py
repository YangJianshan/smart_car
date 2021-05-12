# !/usr/bin/python3
# coding=utf-8

"""
协议形如：
    命令：{"method": "gps_rf_switch", "operate": "setting", "param": {"is_open": true}}
    应答：{"status": "", "method": "", "message": "", "result": ""}
"""


from flask import request
from flask_restful import Api, Resource, reqparse
from app import app
from car import Driver
from pan_tilt import PanTilt as Pt
import json
api = Api(app)


@api.resource('/car')
class Car(Resource):
    driver = Driver()

    @staticmethod
    def post():
        command = request.get_json(force=True)

        method, status, result = Car.driver.do_command(command)
        return {'method': method, 'status': method, 'result': result}
        pass
    pass


@api.resource('/pan-tilt')
class PanTilt(Resource):
    pan_tilt = Pt()

    @staticmethod
    def post():
        command = request.get_json(force=True)
        method, status, result = PanTilt.pan_tilt.do_command(command)
        return {'method': method, 'status': method, 'result': result}
    pass
