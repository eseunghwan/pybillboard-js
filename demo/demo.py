# -*- coding: UTF-8 -*-
import os, sys; demo_dir = os.path.dirname(os.path.abspath(__file__))
import pandas as pd

try:
    from pybillboard_js.billboarder import *
except ImportError:
    sys.path.append(os.path.dirname(demo_dir))
    from pybillboard_js.billboarder import *

tbl_source = pd.DataFrame([[1, 2], [3, 4], [5, 6]], columns = ["A", "B"])
tbl_source_range = pd.DataFrame([[[0, 1, 2], [1, 2, 3]], [[2, 3, 4], [3, 4, 5]], [[4, 5, 6], [5, 6, 7]]], columns = ["A", "B"])
tbl_source_gauge = pd.DataFrame([1], columns = ["A"])

import shutil
shutil.rmtree(os.path.join(demo_dir, "results"), ignore_errors = True)
os.mkdir(os.path.join(demo_dir, "results"))

os.chdir(os.path.join(demo_dir, "results"))
# default types
line_chart = Line(tbl_source); line_chart.export("Line.html")
line_chart.dataframe = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], columns = ["A", "B", "C"]); line_chart.update(True).export("Line_new.html")
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
AreaRange(tbl_source_range).export("AreaRange.html")
Donut(tbl_source).export("Donut.html")
Gauge(tbl_source_gauge).export("Gauge.html")
Radar(tbl_source).export("Radar.html")

MultipleType(tbl_source, {"A": "line", "B": "bar"}).export("MultipleType.html")
