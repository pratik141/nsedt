# -*- coding: utf-8 -*-
"""
Install script
"""
from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as file:
    long_description = file.read()

setup(
    name="nsedt",
    version="0.0.10",
    author="Pratik Anand",
    long_description=long_description,
    long_description_content_type="text/markdown",
    description="Library to collect NSE data in pandas dataframe",
    packages=find_packages(),
    url="https://github.com/pratik141/nsedt",
    install_requires=[
        "requests",
        "numpy",
        "pandas",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
