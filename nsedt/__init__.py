"""
Main file
"""
import logging
from nsedt.resources import constants as cns

logging.basicConfig(
    level=logging.INFO,
    format=cns.LOG_FORMAT,
    datefmt="%m/%d/%Y %I:%M:%S %p",
)
