""" Module docstring.

    Author: Ian Davis
"""
import attr


@attr.s
class Point(object):
    x = attr.ib()
    y = attr.ib()
