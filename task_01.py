#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Program that tells time and date."""


import datetime

CURDATE = None


def get_current_date():
    """Takes the imported datetime and stores it in a variable.

    Args:
        none
    Returns:
        (int/long):returns the current local date.
    """

    date = datetime.date.today()
    return date

if __name__ == "__main__":
    CURDATE = get_current_date()
    print CURDATE
