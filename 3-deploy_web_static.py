#!/usr/bin/python3
<<<<<<< HEAD
# Fabfile to create and distribute an archive to a web server.
import os.path
from datetime import datetime
from fabric.api import env
from fabric.api import local
from fabric.api import put
from fabric.api import run

env.hosts = ["104.196.168.90", "35.196.46.172"]


def do_pack():
    """Create a tar gzipped archive of the directory web_static."""
    dt = datetime.utcnow()
    file = "versions/web_static_{}{}{}{}{}{}.tgz".format(dt.year,
                                                         dt.month,
                                                         dt.day,
                                                         dt.hour,
                                                         dt.minute,
                                                         dt.second)
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(file)).failed is True:
        return None
    return file


def do_deploy(archive_path):
    """Distributes an archive to a web server.
    Args:
        archive_path (str): The path of the archive to distribute.
    Returns:
        If the file doesn't exist at archive_path or an error occurs - False.
        Otherwise - True.
    """
    if os.path.isfile(archive_path) is False:
        return False
    file = archive_path.split("/")[-1]
    name = file.split(".")[0]

    if put(archive_path, "/tmp/{}".format(file)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/".
           format(name)).failed is True:
        return False
    if run("mkdir -p /data/web_static/releases/{}/".
           format(name)).failed is True:
        return False
    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
           format(file, name)).failed is True:
        return False
    if run("rm /tmp/{}".format(file)).failed is True:
        return False
    if run("mv /data/web_static/releases/{}/web_static/* "
           "/data/web_static/releases/{}/".format(name, name)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/web_static".
           format(name)).failed is True:
        return False
    if run("rm -rf /data/web_static/current").failed is True:
        return False
    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
           format(name)).failed is True:
        return False
    return True


def deploy():
    """Create and distribute an archive to a web server."""
    file = do_pack()
    if file is None:
        return False
    return do_deploy(file)
=======
""" Fabric script """
from fabric.api import env, put, run, local
from datetime import datetime
import os


env.hosts = ['34.75.224.91', '3.87.81.24']


def do_pack():
    """ Generates a .tgz file from the contents of 'web_static' folder"""
    now = datetime.now()
    local('mkdir -p versions')
    result = local('tar -cvzf versions/web_static_{}.tgz ./web_static/'.format(
        now.strftime('%Y%m%d%H%M%S')))
    if result.succeeded:
        return 'versions/web_static_{}.tgz web_static/'.format(
            now.strftime('%Y%m%d%H%M%S'))
    else:
        return None


def do_deploy(archive_path):
    """ distributes an archive to the servers """
    if not os.path.exists(archive_path):
        return False

    dest_dir = '/data/web_static/releases/'
    aux = archive_path.split('/')[1]
    file_name = aux.split('.')[0]
    dest_file = dest_dir + file_name

    try:
        put(archive_path, '/tmp')
        run('mkdir -p {}'.format(dest_file))
        run('tar -xzf /tmp/{}.tgz -C {}'.format(file_name, dest_file))
        run('rm -f /tmp/{}.tgz'.format(file_name))
        run('mv {}/web_static/* {}/'.format(dest_file, dest_file))
        run('rm -rf {}/web_static/*'.format(dest_file))
        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(dest_file))
        print("New version deployed!")
        return True
    except:
        return False


def deploy():
    """ Uses above functions for full deployment """
    file_path = do_pack()
    if file_path is None:
        return False
    val = do_deploy(file_path)
    return val
>>>>>>> 1aa7c1466d9987c8ee2e2d156b5bb710c6c822b1
