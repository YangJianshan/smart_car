# !/usr/bin/python3
# coding=utf-8

import RPi.GPIO as GPIO
import time


class Car(object):
    def __init__(self):
        self.__init_gpio()
        pass

    def __init_gpio(self):
        GPIO.setmode(GPIO.BCM)

        GPIO.setup(13, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(6, GPIO.OUT, initial=GPIO.LOW)

        GPIO.setup(26, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(19, GPIO.OUT, initial=GPIO.LOW)

        GPIO.setup(12, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(16, GPIO.OUT, initial=GPIO.LOW)

        GPIO.setup(20, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(21, GPIO.OUT, initial=GPIO.LOW)

        pass

    def __wheel_left_front(self, direction):
        """
        左前轮 20 21
        :param direction: 0=停止 1=前进 -1=后退
        :return:
        """
        if 0 == direction:  # 停止
            GPIO.output(20, GPIO.LOW)
            GPIO.output(21, GPIO.LOW)
        elif 1 == direction:  # 前进
            GPIO.output(20, GPIO.HIGH)
            GPIO.output(21, GPIO.LOW)
        elif -1 == direction:  # 后退
            GPIO.output(20, GPIO.LOW)
            GPIO.output(21, GPIO.HIGH)
        pass

    def __wheel_right_front(self, direction):
        """
        右前轮 12 16
        :param direction:
        :return:
        """
        if 0 == direction:  # 停止
            GPIO.output(12, GPIO.LOW)
            GPIO.output(16, GPIO.LOW)
        elif 1 == direction:  # 前进
            GPIO.output(12, GPIO.LOW)
            GPIO.output(16, GPIO.HIGH)
        elif -1 == direction:  # 后退
            GPIO.output(12, GPIO.HIGH)
            GPIO.output(16, GPIO.LOW)
        pass

    def __wheel_left_rear(self, direction):
        """
        左后轮 19 26
        :param direction:
        :return:
        """
        if 0 == direction:  # 停止
            GPIO.output(19, GPIO.LOW)
            GPIO.output(26, GPIO.LOW)
        elif 1 == direction:  # 前进
            GPIO.output(19, GPIO.LOW)
            GPIO.output(26, GPIO.HIGH)
        elif -1 == direction:  # 后退
            GPIO.output(19, GPIO.HIGH)
            GPIO.output(26, GPIO.LOW)
        pass

    def __wheel_right_rear(self, direction):
        """
        右后轮 6 13
        :param direction:
        :return:
        """
        if 0 == direction:  # 停止
            GPIO.output(6, GPIO.LOW)
            GPIO.output(13, GPIO.LOW)
        elif 1 == direction:  # 前进
            GPIO.output(6, GPIO.HIGH)
            GPIO.output(13, GPIO.LOW)
        elif -1 == direction:  # 后退
            GPIO.output(6, GPIO.LOW)
            GPIO.output(13, GPIO.HIGH)
        pass

    def straight_ahead(self, operate, param):
        """
        直行
        :param operate:
        :param param:
        :return:
        """
        param.setdefault('direction', None)
        direction = param['direction']
        if 'set' == operate:
            if 'ahead' == direction:  # 向前
                self.__wheel_left_front(1)
                self.__wheel_right_front(1)
                self.__wheel_left_rear(1)
                self.__wheel_right_rear(1)
                pass
            elif 'backward' == direction:  # 向后
                self.__wheel_left_front(-1)
                self.__wheel_right_front(-1)
                self.__wheel_left_rear(-1)
                self.__wheel_right_rear(-1)
                pass
            else:
                self.stop('set', None)
                pass
        else:
            pass
        pass

    def side_way(self, operate, param):
        """
        侧行
        :param operate:
        :param param:
        :return:
        """
        param.setdefault('direction', None)
        direction = param['direction']
        if 'set' == operate:
            if 'left' == direction:  # 向左
                self.__wheel_left_front(-1)
                self.__wheel_right_front(1)
                self.__wheel_left_rear(1)
                self.__wheel_right_rear(-1)
                pass
            elif 'right' == direction:  # 向右
                self.__wheel_left_front(1)
                self.__wheel_right_front(-1)
                self.__wheel_left_rear(-1)
                self.__wheel_right_rear(1)
                pass
            else:
                self.stop('set', None)
                pass
        else:
            pass
        pass

    def diagonal(self, operate, param):
        """
        走对角线
        :param operate:
        :param param:
        :return:
        """
        param.setdefault('direction', None)
        direction = param['direction']
        if 'set' == operate:
            if 'left_ahead' == direction:  # 左前
                self.__wheel_left_rear(1)
                self.__wheel_right_front(1)
                pass
            elif 'right_ahead' == direction:  # 右前
                self.__wheel_left_front(1)
                self.__wheel_right_rear(1)
                pass
            elif 'left_backward' == direction:  # 左后
                self.__wheel_left_front(-1)
                self.__wheel_right_rear(-1)
                pass
            elif 'right_backward' == direction:  # 右后
                self.__wheel_left_rear(-1)
                self.__wheel_right_front(-1)
                pass
            else:
                self.stop('set', None)
                pass
        else:
            pass
        pass

    def concerning(self):
        """
        以一个轮子为轴转动
        :return:
        """
        pass

    def turn_round(self, operate, param):
        """
        掉头
        :param operate:
        :param param:
        :return:
        """
        param.setdefault('direction', None)
        direction = param['direction']
        if 'set' == operate:
            if 'clockwise' == direction:  # 顺时针
                self.__wheel_left_front(1)
                self.__wheel_left_rear(1)
                self.__wheel_right_front(-1)
                self.__wheel_right_rear(-1)
                pass
            elif 'anticlockwise' == direction:  # 逆时针
                self.__wheel_left_front(-1)
                self.__wheel_left_rear(-1)
                self.__wheel_right_front(1)
                self.__wheel_right_rear(1)
                pass
            else:
                self.stop('set', None)
                pass
        else:
            pass
        pass

    def turn_of_axis(self):
        """
        沿一条边的中心点转动
        :return:
        """
        pass

    def stop(self, operate, param):
        """
        停车
        :param operate:
        :param param:
        :return:
        """

        if 'set' == operate:
            self.__wheel_left_front(0)
            self.__wheel_right_front(0)
            self.__wheel_left_rear(0)
            self.__wheel_right_rear(0)
        pass

    pass

#
# # 测试
# if __name__ == '__main__':
#     car = Car()
#     car.straight_ahead('set', {'direction': 'ahead'})
#     time.sleep(5)
#     car.stop('set', None)
#     pass
