# -*- coding: UTF-8 -*-
from setuptools import setup, find_packages

setup(
    name = "pybillboard_js",
    version = "0.1.0.alpha7-20180801",
    author = "eseunghwan",
    author_email = "shlee0290@naver.com",
    license = "MIT",
    description = "simple python wrapper for naver billboard.js",
    long_description = open("README.md", "r", encoding = "utf-8").read(),
    long_description_content_type = "text/markdown",
    packages = find_packages(exclude = ["demo"]),
    include_package_data = True,
    python_requires = ">=3.6",
    install_requires = [mname.strip() for mname in open("requirements.txt", "r", encoding = "utf-8").read().strip().split("\n")],
    url = "https://github.com/eseunghwan/pybillboard-js"
)
