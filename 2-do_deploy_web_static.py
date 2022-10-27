#!/usr/bin/python3
<<<<<<< HEAD
"""create archive module"""
from genericpath import isdir
from fabric.api import *
from datetime import datetime

def do_deploy(archive_path):
    """new version"""
    env.hosts = ['44.197.231.3', '100.25.4.135']
    
    if isdir(archive_path) is False:
        return False
    try:
        file_n = archive_path.split("/")[-1]
        no_ext = file_n.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, no_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_n, path, no_ext))
        run('rm /tmp/{}'.format(file_n))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))
        run('rm -rf {}{}/web_static'.format(path, no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_ext))
        return True
    except Exception as ex:
=======
""" Fabric script """
from fabric.api import env, put, run
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
        run('sudo mkdir -p {}'.format(dest_file))
        run('sudo tar -xzf /tmp/{}.tgz -C {}'.format(file_name, dest_file))
        run('sudo rm -f /tmp/{}.tgz'.format(file_name))
        run('sudo mv {}/web_static/* {}/'.format(dest_file, dest_file))
        run('sudo rm -rf {}/web_static/*'.format(dest_file))
        run('sudo rm -rf /data/web_static/current')
        run('sudo ln -s {} /data/web_static/current'.format(dest_file))
        print("New version deployed!")
        return True
    except:
>>>>>>> 1aa7c1466d9987c8ee2e2d156b5bb710c6c822b1
        return False
