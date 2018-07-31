# -*- coding: UTF-8 -*-
import os, sys; demo_dir = os.path.dirname(os.path.abspath(__file__))
import pandas as pd
from random import uniform, randint

try:
    from pybillboard_js.billboarder import *
except ImportError:
    sys.path.append(os.path.dirname(demo_dir))
    from pybillboard_js.billboarder import *


# default source dataframe
tbl_source = pd.DataFrame([[uniform(0, 10), uniform(0, 10)] for i in range(10)], columns = ["A", "B"])
# range style dataframe
tbl_source_range = pd.DataFrame()
for col in tbl_source.columns:
    tbl_source_range[col] = [[value * 0.8, value, value * 1.2] for value in tbl_source[col].values]

# gauge-targeted dataframe
tbl_source_gauge = pd.DataFrame([randint(0, 100)], columns = ["A"])

import shutil
shutil.rmtree(os.path.join(demo_dir, "results"), ignore_errors = True)
os.mkdir(os.path.join(demo_dir, "results"))

os.chdir(os.path.join(demo_dir, "results"))
# default types
line_chart = Line(tbl_source); line_chart.export("Line.html")
line_chart.dataframe = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], columns = ["A", "B", "C"]); line_chart.update(return_class = True).export("Line_new.html")
Bar(tbl_source).export("Bar.html"); Bar(tbl_source, stack = True).export("Bar_stack.html")
Area(tbl_source).export("Area.html"); Area(tbl_source, stack = True).export("Area_stack.html")
Scatter(tbl_source).export("Scatter.html")
Pie(tbl_source).export("Pie.html")
Bubble(tbl_source).export("Bubble.html")

# advanced types
SpLine(tbl_source).export("SpLine.html")
AreaSpLine(tbl_source).export("AreaSpLine.html")
Step(tbl_source).export("Step.html")
AreaStep(tbl_source).export("AreaStep.html")
AreaLineRange(tbl_source).export("AreaLineRange.html") # if generate range chart with default style dataframe, automatically transform dataframe style into range style
AreaSpLineRange(tbl_source_range).export("AreaSpLineRange.html")
Donut(tbl_source).export("Donut.html")
Gauge(tbl_source_gauge).export("Gauge.html")
Radar(tbl_source).export("Radar.html")

MultipleType(tbl_source, {"A": "Line", "B": "Bar"}).export("MultipleType.html")
