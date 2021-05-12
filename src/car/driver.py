# !/usr/bin/python3
# coding=utf-8


from .car import Car


class Driver(object):
    def __init__(self):
        self.__car = Car()
        self.__car.stop('set', None)
        pass

    def do_command(self, command):
        """

        :param command:
        :return:
        """
        command.setdefault('method', None)
        command.setdefault('operate', None)
        command.setdefault('param', None)
        method = command['method']
        if 'stop' == method:
            result = self.__car.stop(command['operate'], command['param'])
            pass
        elif 'straight_ahead' == method:  # 向前
            result = self.__car.straight_ahead(command['operate'], command['param'])
            pass
        elif 'side_way' == method:  # 横向
            result = self.__car.side_way(command['operate'], command['param'])
            pass
        elif 'diagonal' == method:  # 对角线
            result = self.__car.diagonal(command['operate'], command['param'])
            pass
        elif 'turn_round' == method:  # 转向
            result = self.__car.turn_round(command['operate'], command['param'])
            pass
        else:
            return None, 'error', None

        return method, 'ok', result
        pass

    pass
