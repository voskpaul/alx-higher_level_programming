#!/usr/bin/python3
# date_utils.py

import datetime

def get_current_date():
    """
    This function returns the current date.
    """
    return datetime.date.today()

def get_current_time():
    """
    This function returns the current time.
    """
    return datetime.datetime.now().time()

