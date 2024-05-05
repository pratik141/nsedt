# -*- coding: utf-8 -*-
"""
Install script
"""
import os
from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as file:
    long_description = file.read()

with open("requirements.txt", "r", encoding="utf-8") as f:
    required_lib = f.read().splitlines()

setup(
    name="nsedt",
    version=os.getenv("GITHUB_REF_NAME"),
    author="Pratik Anand",
    long_description=long_description,
    long_description_content_type="text/markdown",
    description="Library to collect NSE data",
    packages=find_packages(),
    url="https://github.com/pratik141/nsedt",
    install_requires=required_lib,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
