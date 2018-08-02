# -*- coding: UTF-8 -*-
import pandas as pd
from .prototypes import Chart
from .functions import get_df_dimension
from copy import deepcopy

### single type charts
## default chart types
# line chart
class Line(Chart):
    def __init__(self, dataframe, options = {}, include_res = True):
        super().__init__(self.__class__.__name__, dataframe, options, include_res)

# area chart(stacked)
class Area(Chart):
    def __init__(self, dataframe, options = {}, include_res = True, stack = False):
        super().__init__(self.__class__.__name__, dataframe, options, include_res, stack = stack)

# bar chart(stacked)
class Bar(Chart):
    def __init__(self, dataframe, options = {}, include_res = True, stack = False):
        super().__init__(self.__class__.__name__, dataframe, options, include_res, stack = stack)

# scatter chart
class Scatter(Chart):
    def __init__(self, dataframe, options = {}, include_res = True):
        super().__init__(self.__class__.__name__, dataframe, options, include_res)

# pie chart
class Pie(Chart):
    def __init__(self, dataframe, options = {}, include_res = True):
        super().__init__(self.__class__.__name__, dataframe, options, include_res)

# bubble chart
class Bubble(Chart):
    def __init__(self, dataframe, options = {}, include_res = True):
        super().__init__(self.__class__.__name__, dataframe, options, include_res)


## advanced chart types
# spline style
class SpLine(Chart):
    def __init__(self, dataframe, options = {}, include_res = True):
        super().__init__(self.__class__.__name__, dataframe, options, include_res)

class AreaSpLine(Chart):
    def __init__(self, dataframe, options = {}, include_res = True):
        super().__init__(self.__class__.__name__, dataframe, options, include_res)

# step style
class Step(Chart):
    def __init__(self, dataframe, options = {}, include_res = True):
        super().__init__(self.__class__.__name__, dataframe, options, include_res)

class AreaStep(Chart):
    def __init__(self, dataframe, options = {}, include_res = True):
        super().__init__(self.__class__.__name__, dataframe, options, include_res)

# area range
class AreaLineRange(Chart):
    def __init__(self, dataframe, options = {}, include_res = True):
        new_dataframe = pd.DataFrame()
        if get_df_dimension(dataframe) < 3:
            for col in dataframe.columns:
                new_dataframe[col] = [[value - 1, value, value + 1] if not isinstance(value, str) and str(value).isdigit() else ["", value, ""] for value in dataframe[col].values]
        else:
            new_dataframe = deepcopy(dataframe)

        super().__init__(self.__class__.__name__, new_dataframe, options, include_res)

class AreaSpLineRange(Chart):
    def __init__(self, dataframe, options = {}, include_res = True):
        new_dataframe = pd.DataFrame()
        if get_df_dimension(dataframe) < 3:
            for col in dataframe.columns:
                new_dataframe[col] = [[value - 1, value, value + 1] if not isinstance(value, str) and str(value).isdigit() else ["", value, ""] for value in dataframe[col].values]
        else:
            new_dataframe = deepcopy(dataframe)

        super().__init__(self.__class__.__name__, new_dataframe, options, include_res)

# dounut
class Donut(Chart):
    def __init__(self, dataframe, options = {}, include_res = True):
        super().__init__(self.__class__.__name__, dataframe, options, include_res)

# gauge
class Gauge(Chart):
    def __init__(self, dataframe, options = {}, include_res = True):
        new_dataframe = pd.DataFrame(
            [dataframe[dataframe.columns[0]].map(float).describe()["mean"]],
            columns = [dataframe.columns[0]]
        )

        super().__init__(self.__class__.__name__, new_dataframe, options, include_res)

# radar
class Radar(Chart):
    def __init__(self, dataframe, options = {}, include_res = True):
        super().__init__(self.__class__.__name__, dataframe, options, include_res)


## multiple(combination) chart
class MultipleType(Chart):
    def __init__(self, dataframe, type_info, options = {}, include_res = True):
        super().__init__(type_info, dataframe, options, include_res)

del Chart