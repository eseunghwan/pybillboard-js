# -*- coding: UTF-8 -*-
import logging

## init logger
Logger = logging.getLogger("BILLBOARD.JS")
Logger.setLevel(logging.INFO)

## set handler
Handler = logging.StreamHandler()
Handler.setFormatter(logging.Formatter("%(name)s::%(levelname)s %(message)s - %(asctime)s"))

Logger.addHandler(Handler)
