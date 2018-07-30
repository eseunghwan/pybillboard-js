# -*- coding: UTF-8 -*-
import os; module_dir = os.path.dirname(os.path.abspath(__file__))
from tinydb import TinyDB, Query

# import logger
from .logger import Logger

config, query = TinyDB(os.path.join(module_dir, "res", "config.db"), default_table = "config", indent = 4), Query()

if config.search(query.NAME == "UPDATE_RES")[0]["VALUE"]:# check for update res
    from .functions import update_res
    update_res()
