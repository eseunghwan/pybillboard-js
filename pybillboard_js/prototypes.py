# -*- coding: UTF-8 -*-
# import pandas
import pandas as pd

class Chart():
    def __init__(self, chart_type = "line", dataframe = pd.DataFrame(), options = {}, include_res = True, **kwargs):
        self._id, self.chart_type, self.dataframe = "billboard-{0}".format(str(self.__hash__()).replace("-", "")), chart_type, dataframe
        self.options, self.include_res = options, include_res
        for key in kwargs.keys():
            exec("self.{0} = kwargs[key]".format(key))
            
        self.generate()

    def __str__(self):
        from lxml.html import tostring
        return tostring(self._root, pretty_print = True, encoding = "utf-8").decode("utf-8")

    def __repr__(self):
        return repr(self._root)
    
    def generate(self):
        from lxml.html import builder as lxhtml
        from .functions import get_js_text

        self._data = {"columns": []}

        if isinstance(self.chart_type, dict):
            self._data["types"] = self.chart_type
            self._class = "MultipleType"
        elif isinstance(self.chart_type, str):
            self._data["type"] = self.chart_type
            self._class = self.chart_type
        else:
            from .exceptions import ChartTypeError
            raise ChartTypeError("invalid type format: {0}".format(self.chart_type))

        if "x" in self.options.keys():
            self._data["x"] = options["x"]
            self.options.pop("x", None)

        try:
            if self.stack:
                self._data["groups"] = [self.dataframe.columns.tolist()]
        except:
            pass

        for col in self.dataframe.columns:
            self._data["columns"].append([col] + self.dataframe[col].values.tolist())

        self._root = lxhtml.DIV(
            lxhtml.CLASS("billboard-{0}".format(self._class)),
            style = "padding: 10px;"
        )

        if self.include_res:
            self._root.append(lxhtml.SCRIPT(get_js_text("billboard-js"), type = "text/javascript"))
            self._root.append(lxhtml.STYLE(get_js_text("billboard-css")))

        self._root.append(lxhtml.DIV(id = self._id))
        self._root.append(
            lxhtml.SCRIPT("""
bb.generate({
    bindto: "#%s",
    data: %s,
    %s
});
""" % (self._id, self._data, ",\n".join(["'{0}': {1}".format(key, value) for key, value in self.options.items()])), type = "text/javascript")
        )

    def update(self, key_name = None, value = None, return_class = False):
        if not key_name == None and not value == None:
            exec("self.{0} = value".format(key_name))

        self.generate()

        if return_class:
            return self

    def render(self):
        return self.__str__()

    def export(self, file_path):
        with open(file_path, "w", encoding = "utf-8") as export_write:
            export_write.write(self.__str__())
