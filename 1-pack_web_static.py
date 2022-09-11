#!/usr/bin/python3
"""Generates a .tgz archive from the contents of the web_static"""

from fabric.api import *
from time import strftime


def do_pack():
    x = strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local("tar -czvf versions/web_static_{}.tgz web_static/".format(x))
        return ("versions/web_static_{}.tgz".format(x))
    except Exception:
        return None
