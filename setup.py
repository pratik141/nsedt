# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name="nsedt",
    version="0.0.2",
    author="Pratik Anand",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    description="Library to collect NSE data in pandas dataframe",
    packages=find_packages(),
    url="https://github.com/pratik141/nsedt",
    install_requires=[
        "requests",
        "numpy",
        "pandas",
        "six",
        "click",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
