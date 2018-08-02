# -*- coding: UTF-8 -*-
import os
from .logger import Logger
from .functions import get_config, get_raw_type
from .exceptions import ChartTypeError, ExportFormatError
# import pandas
import pandas as pd
# import lxml.html
from lxml.html import builder as lxhtml, tostring

class Chart():
    def __init__(self, chart_type = "line", dataframe = pd.DataFrame(), options = {}, include_res = True, stack = False):
        self._cid = str(self.__hash__()).replace("-", "")
        self._id, self.chart_type, self.dataframe = "billboard-{0}".format(self._cid), chart_type, dataframe
        self.options, self.include_res = options, include_res
        self.stack = stack

        self.generate()

    def __str__(self):
        return tostring(self._root, pretty_print = True, encoding = "utf-8").decode("utf-8")

    def __repr__(self):
        return repr(self._root)
    
    def generate(self):
        Logger.info("Generating Chart by id {0}".format(self._cid))
        self._data = {"columns": []}

        if isinstance(self.chart_type, dict):
            self._data["types"] = {key: get_raw_type(value) for key, value in self.chart_type.items()}
            self.raw_type = "MultipleType_{0}".format("_".join(list(self._data["types"].values())))
        elif isinstance(self.chart_type, str):
            self._data["type"] = get_raw_type(self.chart_type)
            self.raw_type = "SingleType_{0}".format(self._data["type"])
        else:
            raise ChartTypeError("invalid type format: {0}".format(self.chart_type))

        if "x" in self.options.keys():
            self._data["x"] = self.options["x"]
            self.options.pop("x", None)

        try:
            if self.stack:
                self._data["groups"] = [self.dataframe.columns.tolist()]
        except:
            pass

        for col in self.dataframe.columns:
            self._data["columns"].append([col] + self.dataframe[col].values.tolist())

        self._root = lxhtml.DIV(
            lxhtml.DIV(id = self._id),
            lxhtml.CLASS("billboard-{0}".format(self.raw_type)),
            style = "padding: 10px;"
        )

        script_text = ""
        if self.include_res:
            self._root.append(lxhtml.SCRIPT(get_config("billboard-js"), id = "{0}-js".format(self._id)))
            self._root.append(lxhtml.STYLE(get_config("billboard-css"), id = "{0}-css".format(self._id)))

            script_text += """
if (document.getElementById("billboard-js") == null && document.getElementById("billboard-css") == null) {
    var billboard_js = document.createElement("script"), billboard_css = document.createElement("style");
    billboard_js.id = "billboard-js", billboard_css.id = "billboard-css";

    billboard_js.appendChild(document.createTextNode(document.getElementById("%(js_id)s").text));
    billboard_css.appendChild(document.createTextNode(document.getElementById("%(css_id)s").innerText));

    document.head.appendChild(billboard_js);
    document.head.appendChild(billboard_css);
}

document.getElementById("%(js_id)s").remove();
document.getElementById("%(css_id)s").remove();
""" % {"js_id": "{0}-js".format(self._id), "css_id": "{0}-css".format(self._id)}

        script_text += """
bb.generate({
    bindto: "#%s",
    data: %s,
    %s
});
""" % (self._id, self._data, ",\n".join(["'{0}': {1}".format(key, value) for key, value in self.options.items()]))

        self._root.append(lxhtml.SCRIPT(script_text, type = "text/javascript", id = "{0}-script".format(self._id), onload = "eval(this.text);"))

        Logger.info("Generated Chart {0}".format(self.raw_type))

    def update(self, key_name = None, value = None, return_class = True):
        if not key_name == None and not value == None:
            Logger.info("Update {0} as {1}".format(key_name, value))
            exec("self.{0} = value".format(key_name))

        Logger.info("Regenerate Chart")
        self.generate()

        if return_class:
            return self

    def render(self):
        Logger.info("Render Chart to html string")
        return self.__str__()

    def export(self, file_path = None):
        if file_path == None:
            file_path = "{0}.html".format(self.raw_type)

        file_path = os.path.abspath(file_path)
        file_format = os.path.splitext(file_path)[-1][1:]

        if file_format in ["html"]:
            with open(file_path, "w", encoding = "utf-8") as export_write:
                if file_format == "html":
                    Logger.info("Export to {0}".format(os.path.basename(file_path)))
                else:
                    Logger.info("Support only html for export type")

                export_write.write(self.__str__())
        else:
            raise ExportFormatError("Invalid export file format: {0}".format(file_format))

        
