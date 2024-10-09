# strategy/utils.py

import logging
import os
import sys

def setup_logging():
    logging.basicConfig(
        filename='C:\git\StratTester\logs\strategy.log',
        level=logging.INFO,
        format='%(asctime)s [%(levelname)s] %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

def log_exception(e):
    logging.error("Exception occurred", exc_info=True)
