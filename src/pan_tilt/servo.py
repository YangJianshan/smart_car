# !/usr/bin/python3
# coding=utf-8

"""
舵机
"""
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)


class Servo(object):
    def __init__(self, pin):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.OUT)
        self.__pin = pin
        pass

    def set_angle(self, angle):
        """
        :param angle:
        :return:
        """
        pwm = GPIO.PWM(self.__pin, 50)
        pwm.start(0)
        pwm.ChangeDutyCycle(angle / 18+2.5)
        time.sleep(.03)
        pwm.stop()
        return angle
        pass

    pass


# if '__main__' == __name__:
#     s = Servo(2)
#     for angle in range(30, 170, 10):
#         print(angle)
#         s.set_angle(angle)
#     time.sleep(120)
#     GPIO.cleanup()

