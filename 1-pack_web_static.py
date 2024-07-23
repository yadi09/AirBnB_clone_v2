#!/usr/bin/python3
"""Fabric script that generates a .tgz archive
from the contents of the web_static folder"""

from fabric.api import local
from datetime import datetime

def do_pack():
    """Fabric script that generates a .tgz archive"""
    local("mkdir -p versions")
    time = datetime.now()
    file_path = "versions/web_static_{}{}{}{}{}{}.tgz".format(
        time.year,
        time.month,
        time.day,
        time.hour,
        time.minute,
        time.second
    )

    try:
        local("tar -czvf {} web_static".format(file_path))
    except Exception:
        file_path = None

    return file_path
