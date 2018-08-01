# -*- coding: UTF-8 -*-
class ChartTypeError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value

class ExportFormatError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value
