# -*- coding: UTF-8 -*-
from .prototypes import Chart

### single type charts
## default chart types
# line chart
class Line(Chart):
    def __init__(self, dataframe, options = {}, include_res = True):
        super().__init__("line", dataframe, options, include_res)

# area chart
class Area(Chart):
    def __init__(self, dataframe, options = {}, include_res = True, stack = False):
        super().__init__("area", dataframe, options, include_res, stack = stack)

# bar chart
class Bar(Chart):
    def __init__(self, dataframe, options = {}, include_res = True, stack = False):
        super().__init__("bar", dataframe, options, include_res, stack = stack)

# scatter chart
class Scatter(Chart):
    def __init__(self, dataframe, options = {}, include_res = True):
        super().__init__("scatter", dataframe, options, include_res)

# pie chart
class Pie(Chart):
    def __init__(self, dataframe, options = {}, include_res = True):
        super().__init__("pie", dataframe, options, include_res)

# bubble chart
class Bubble(Chart):
    def __init__(self, dataframe, options = {}, include_res = True):
        super().__init__("bubble", dataframe, options, include_res)


## advanced chart types
# spline style
class SpLine(Chart):
    def __init__(self, dataframe, options = {}, include_res = True):
        super().__init__("spline", dataframe, options, include_res)

class AreaSpLine(Chart):
    def __init__(self, dataframe, options = {}, include_res = True):
        super().__init__("area-spline", dataframe, options, include_res)

# step style
class Step(Chart):
    def __init__(self, dataframe, options = {}, include_res = True):
        super().__init__("step", dataframe, options, include_res)

class AreaStep(Chart):
    def __init__(self, dataframe, options = {}, include_res = True):
        super().__init__("area-step", dataframe, options, include_res)

# area range
class AreaRange(Chart):
    def __init__(self, dataframe, options = {}, include_res = True):
        super().__init__("area-line-range", dataframe, options, include_res)

# dounut
class Donut(Chart):
    def __init__(self, dataframe, options = {}, include_res = True):
        super().__init__("donut", dataframe, options, include_res)

# gauge
class Gauge(Chart):
    def __init__(self, dataframe, options = {}, include_res = True):
        super().__init__("gauge", dataframe[dataframe.columns[0]].to_frame() if len(dataframe.columns) > 1 else dataframe, options, include_res)

# radar
class Radar(Chart):
    def __init__(self, dataframe, options = {}, include_res = True):
        super().__init__("radar", dataframe, options, include_res)


## multiple(combination) chart
class MultipleType(Chart):
    def __init__(self, dataframe, type_info, options = {}, include_res = True):
        super().__init__(type_info, dataframe, options, include_res)

del Chart