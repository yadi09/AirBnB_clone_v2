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
    path = "/data/web_static/releases/{}/".format(unzip_file)

    try:
        put(archive_path, '/tmp/')

        run("mkdir -p /data/web_static/releases/{}".format(unzip_file))
        run("tar -xzvf /tmp/{} -C {}".format(
            file_name,
            path
        ))
        run("rm -rf /tmp/{}".format(file_name))
        run("mv {}web_static/* {}".format(path, path))
        run("rm -rf /data/web_static/releases/{}/web_static"
            .format(unzip_file))
        run("rm /data/web_static/current")
        run("ln -s /data/web_static/releases/{} /data/web_static/current"
            .format(unzip_file))

        return True
    except Exception:
        return False
