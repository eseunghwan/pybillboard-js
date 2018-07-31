# pybillboard_js

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Open Source Love](https://badges.frapsoft.com/os/mit/mit.svg?v=102)](https://github.com/ellerbrock/open-source-badge/)

simple python wrapper for naver billboard.js

[<img src="https://naver.github.io/billboard.js/img/logo/billboard.js.svg" width="350" alt="billboard.js">](https://github.com/naver/billboard.js)

## Install
```
pip3 install pybillboard-js
or
python3 -m pip install pybillboard-js
```

## Usage
### import billboarder(chart builder)
```
from pybillboard_js.billboarder import *
```

### generate chart and render
```
line_chart = Line(some_dataframe)      <- returns lxml.html tree object
line_chart.render()                    <- returns lxml.html tostring result
line_chart.export(some_path)           <- export render() result to destination file
```

### update chart data or options
```
line_chart.dataframe = some_other_dataframe
line_chart.update()                   <- returns result like generate chart
```

##### or simply use all scripts at once
```
Line(some_dataframe).update("dataframe", some_other_dataframe).export(some_path)
```

## Available Chart Types
### simple chart types
Line, Area, Bar, Scatter, Pie, Bubble

### advanced chart types
SpLine, AreaSpLine, Step, AreaStep, AreaRange, Donut, Gauge, Radar

### and multiple combination
MultipleType


## Demo
You can find demo on [demo](https://github.com/eseunghwan/pybillboard_js/tree/master/demo)

## Bug report and Q&A
If you find bugs or have questions, please notice [issues](https://github.com/eseunghwan/pybillboard_js/issues) on Github
