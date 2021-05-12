# !/usr/bin/python3
# coding=utf-8

"""
云台
"""
from pan_tilt.servo import Servo


class PanTilt(object):
    def __init__(self):
        self.__pitch_servo = Servo(2)
        self.__horizontal_servo = Servo(3)
        pass

    def __servo_pitch(self, operate, param):
        angle = param['angle']
        if 'set' == operate:
            self.__pitch_servo.set_angle(angle)
        return angle
        pass

    def __servo_horizontal(self, operate, param):
        angle = param['angle']
        if 'set' == operate:
            self.__horizontal_servo.set_angle(angle)
        return angle
        pass

    def do_command(self, command):
        method = command['method']
        if 'pitch' == method:
            angle = self.__servo_pitch(command['operate'], command['param'])
            pass
        elif 'horizontal' == method:
            angle = self.__servo_horizontal(command['operate'], command['param'])
            pass
        else:
            pass
        return method, 'ok', {'angle': angle}
        pass

    pass
