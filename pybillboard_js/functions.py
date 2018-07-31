# -*- coding: UTF-8 -*-
# import os
import os; module_dir = os.path.dirname(os.path.abspath(__file__))
# import config
from . import config, query
# import logger
from .logger import Logger

# function update_res
def update_res():
    import wget

    if os.path.exists(os.path.join(module_dir, "res", "billboard.js")):
        os.remove(os.path.join(module_dir, "res", "billboard.js"))

    if os.path.exists(os.path.join(module_dir, "res", "billboard.css")):
        os.remove(os.path.join(module_dir, "res", "billboard.css"))
    
    Logger.info("Update resources")
    # download billboard.min.js
    wget.download("https://naver.github.io/billboard.js/release/latest/dist/billboard.pkgd.min.js", os.path.join(module_dir, "res", "billboard.js"))

    # download billboard.min.css
    wget.download("https://naver.github.io/billboard.js/release/latest/dist/billboard.min.css", os.path.join(module_dir, "res", "billboard.css"))

    # change update_res to false
    config.update({"VALUE": False}, query.NAME == "UPDATE_RES")

# function get_js_text
def get_js_text(category):
    if category == "billboard-js":
        source_path = os.path.join(module_dir, "res", "billboard.js")
    elif category == "billboard-css":
        source_path = os.path.join(module_dir, "res", "billboard.css")

    with open(source_path, "r", encoding = "utf-8") as source_read:
        source_text = source_read.read()

    return source_text

# function get_raw_type
def get_raw_type(pybillboard_chart_type):
    chart_type_info = {
        "Line": "line",
        "Area": "area",
        "Bar": "bar",
        "Scatter": "scatter",
        "Pie": "pie",
        "Bubble": "bubble",
        "SpLine": "spline",
        "AreaSpLine": "area-spline",
        "Step": "step",
        "AreaStep": "area-step",
        "AreaLineRange": "area-line-range",
        "AreaSpLineRange": "area-spline-range",
        "Donut": "donut",
        "Gauge": "gauge",
        "Radar": "radar"
    }

    if pybillboard_chart_type in chart_type_info.keys():
        return chart_type_info[pybillboard_chart_type]
    else:
        from .exceptions import ChartTypeError
        raise ChartTypeError("invalid chart type: {0}".format(pybillboard_chart_type))

# function get_df_dimension
def get_df_dimension(dataframe):
    import numpy as np
    
    return len(np.array(dataframe.values.tolist()).shape)
