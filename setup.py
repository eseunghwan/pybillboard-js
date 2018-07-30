# -*- coding: UTF-8 -*-
from setuptools import setup, find_packages

setup(
    name = "pybillboard_js",
    version = "0.1.0.alpha1",
    author = "eseunghwan",
    author_email = "shlee0290@naver.com",
    license = "MIT",
    description = "simple python wrapper for naver billboard.js",
    long_description = open("README.md").read(),
    packages = find_packages(exclude = ["demo"]),
    python_requires = ">=3.6",
    url = "https://github.com/eseunghwan/pybillboard_js"
)
