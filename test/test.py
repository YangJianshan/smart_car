# !/usr/bin/python
# coding=utf-8
import time

try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print('GPIO 导入错误')

GPIO.setmode(GPIO.BCM)


def setServoAngle(servo, angle):
    pwm = GPIO.PWM(servo, 50)
    pwm.start(0)
    dutyCycle = angle / 18. + 3.
    pwm.ChangeDutyCycle(dutyCycle)
    time.sleep(0.3)
    pwm.stop()

# GPIO.setup(13, GPIO.OUT, initial=GPIO.LOW)
# GPIO.setup(6, GPIO.OUT, initial=GPIO.LOW)
#
# GPIO.setup(26, GPIO.OUT, initial=GPIO.LOW)
# GPIO.setup(19, GPIO.OUT, initial=GPIO.LOW)
#
# GPIO.setup(12, GPIO.OUT, initial=GPIO.LOW)
# GPIO.setup(16, GPIO.OUT, initial=GPIO.LOW)
#
# GPIO.setup(20, GPIO.OUT, initial=GPIO.LOW)
# GPIO.setup(21, GPIO.OUT, initial=GPIO.LOW)
# while True:
#     print('......')
#     time.sleep(1)


if __name__ == '__main__':
    import sys
    GPIO.setup(3, GPIO.OUT)
    setServoAngle(3, 90)
    GPIO.cleanup()


