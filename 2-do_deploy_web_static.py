#!/usr/bin/python3
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
        return False
