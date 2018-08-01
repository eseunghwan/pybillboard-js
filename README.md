# pybillboard_js

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Open Source Love](https://badges.frapsoft.com/os/mit/mit.svg?v=102)](https://github.com/ellerbrock/open-source-badge/)

simple python wrapper for naver billboard.js

[<img src="https://naver.github.io/billboard.js/img/logo/billboard.js.svg" width="350" alt="billboard.js"></img>](https://github.com/naver/billboard.js)

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
line_chart.update()        <- returns result like generate chart
```

##### or simply use all scripts at once
```
Line(some_dataframe).update("dataframe", some_other_dataframe).export(some_path)
```

## Available Chart Types
### simple chart types
##### Line
<img src="https://github.com/eseunghwan/pybillboard-js/blob/master/demo/images/Line.png"></img>
```
Line(some_dataframe).export(some_path)
```
##### Area
<img src="https://github.com/eseunghwan/pybillboard-js/blob/master/demo/images/Area.png"></img>
```
Area(some_dataframe).export(some_path)
```
##### Bar
<img src="https://github.com/eseunghwan/pybillboard-js/blob/master/demo/images/Bar.png"></img>
```
Bar(some_dataframe).export(some_path)
```
##### Scatter
<img src="https://github.com/eseunghwan/pybillboard-js/blob/master/demo/images/Scatter.png"></img>
```
Scatter(some_dataframe).export(some_path)
```
##### Pie
<img src="https://github.com/eseunghwan/pybillboard-js/blob/master/demo/images/Pie.png"></img>
```
Pie(some_dataframe).export(some_path)
```
##### Bubble
<img src="https://github.com/eseunghwan/pybillboard-js/blob/master/demo/images/Bubble.png"></img>
```
Bubble(some_dataframe).export(some_path)
```

### stacked charts
##### Area Stack
<img src="https://github.com/eseunghwan/pybillboard-js/blob/master/demo/images/Area_stack.png"></img>
```
Area(some_dataframe, stack = True).export(some_path)
```
##### Bar Stack
<img src="https://github.com/eseunghwan/pybillboard-js/blob/master/demo/images/Bar_stack.png"></img>
```
Bar(some_dataframe, stack = True).export(some_path)
```

### advanced chart types
##### SpLine
<img src="https://github.com/eseunghwan/pybillboard-js/blob/master/demo/images/SpLine.png"></img>
```
SpLine(some_dataframe).export(some_path)
```
##### AreaSpLine
<img src="https://github.com/eseunghwan/pybillboard-js/blob/master/demo/images/AreaSpLine.png"></img>
```
AreaSpLine(some_dataframe).export(some_path)
```
##### Step
<img src="https://github.com/eseunghwan/pybillboard-js/blob/master/demo/images/Step.png"></img>
```
Step(some_dataframe).export(some_path)
```
##### AreaStep
<img src="https://github.com/eseunghwan/pybillboard-js/blob/master/demo/images/AreaStep.png"></img>
```
AreaStep(some_dataframe).export(some_path)
```
##### AreaLineRange
<img src="https://github.com/eseunghwan/pybillboard-js/blob/master/demo/images/AreaLineRange.png"></img>
```
AreaLineRange(some_dataframe).export(some_path)
```
##### AreaSpLineRange
<img src="https://github.com/eseunghwan/pybillboard-js/blob/master/demo/images/AreaSpLineRange.png"></img>
```
AreaSpLineRange(some_dataframe).export(some_path)
```
##### Donut
<img src="https://github.com/eseunghwan/pybillboard-js/blob/master/demo/images/Donut.png"></img>
```
Donut(some_dataframe).export(some_path)
```
##### Gauge
<img src="https://github.com/eseunghwan/pybillboard-js/blob/master/demo/images/Gauge.png"></img>
```
Gauge(some_dataframe).export(some_path)
```
##### Radar
<img src="https://github.com/eseunghwan/pybillboard-js/blob/master/demo/images/Radar.png"></img>
```
Radar(some_dataframe).export(some_path)
```

### and multiple combination
<img src="https://github.com/eseunghwan/pybillboard-js/blob/master/demo/images/MultipleType.png"></img>
```
MultipleType(some_dataframe, dictionary_style_type_info).export(some_path)
```


## Demo
You can find demo on [demo](https://github.com/eseunghwan/pybillboard_js/tree/master/demo)

## Bug report and Q&A
If you find bugs or have questions, please notice [issues](https://github.com/eseunghwan/pybillboard_js/issues) on Github
