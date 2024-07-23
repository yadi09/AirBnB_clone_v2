#!/usr/bin/python3
"""Fabric script that generates a .tgz archive
from the contents of the web_static folder"""

from fabric.api import local, env, put, run
from datetime import datetime
import os


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

def do_deploy(archive_path):
    """Fabric script that distributes an archive to your web servers,"""
    if not os.path.exists(archive_path):
        return False

    env.hosts = ['ubuntu@52.201.211.145', 'ubuntu@54.209.162.93']

    file_name = archive_path.split('/')[-1]
    unzip_file = file_name.replace(".tgz", "")
    
    try:
        put(archive_path, '/tmp/')

        run("mkdir -p /data/web_static/releases/{}".format(unzip_file))
        run("tar -xzvf /tmp/{} -C /data/web_static/releases/{}".format(
            file_name,
            unzip_file
        ))

        run("rm /tmp/{}".format(file_name))
        run("rm /data/web_static/current")
        run("ln -s /data/web_static/releases/{} /data/web_static/current".format(
            unzip_file
        ))
        run("mv /data/web_static/current/web_static/* /data/web_static/current/")
        run("rm -r /data/web_static/current/web_static")
        return True
    except Exception:
        return False
