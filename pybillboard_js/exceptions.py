# -*- coding: UTF-8 -*-
class ChartTypeError(Message):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value
