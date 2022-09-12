#!/usr/bin/python3
"""Creates and distributes an archive to your web servers"""

from fabric.api import *
from time import strftime
from os import path
env.hosts = ['54.196.227.13', '54.234.49.207']


def do_pack():
    """create compress file with time format(x)"""
    x = strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local("tar -czvf versions/web_static_{}.tgz web_static/".format(x))
        return ("versions/web_static_{}.tgz".format(x))
    except Exception:
        return None


def do_deploy(archive_path):
    """distributes an archive to your web servers"""

    if (path.isfile(archive_path) is False):
        return False

    try:
        file_path = archive_path.split("/")[-1]
        uncom_file = ("/data/web_static/releases/" + file_path.split(".")[0])
        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}".format(uncom_file))
        run("sudo tar -xzf /tmp/{} -C {}".format(file_path, uncom_file))
        run("sudo rm /tmp/{}".format(file_path))
        run("sudo mv {}/web_static/* {}/".format(uncom_file, uncom_file))
        run("sudo rm -rf {}/web_static".format(uncom_file))
        run('sudo rm -rf /data/web_static/current')
        run("sudo ln -s {} /data/web_static/current".format(uncom_file))
        return True
    except Exception:
        return False


def deploy():
    """Creates and distributes an archive to your web servers"""
    try:
        created_archive = do_pack()
        value = do_deploy(created_archive)
        return value
    except Exception:
        return False
