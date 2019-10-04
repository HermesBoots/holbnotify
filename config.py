#!/usr/bin/env python3
"""Configure ini file for future use in program"""
import configparser
from holbnotify import Creds
import os.path


def config(path):
    """Configures the init file for the program

    Args:
        path (str): Path to the ini file

    Return:
        (Creds) object with credentials (Success)
    """
    if not os.path.isfile(path):
        raise(OSError("File not found"))
    parse = configparser.ConfigParser()
    parse.read(path)
    ret = Creds(
        parse['DEFAULT']['api_key'],
        parse['DEFAULT']['email'],
        parse['DEFAULT']['password']
    )
    return ret
