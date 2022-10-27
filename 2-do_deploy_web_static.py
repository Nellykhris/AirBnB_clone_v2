#!/usr/bin/python3
<<<<<<< HEAD
"""create archive module"""
from genericpath import isdir
from fabric.api import *
=======
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
>>>>>>> 830f3165d26ad344d8816074a4a526094e54309c
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
<<<<<<< HEAD
    except Exception as ex;
=======
    except:
>>>>>>> 1aa7c1466d9987c8ee2e2d156b5bb710c6c822b1
>>>>>>> 830f3165d26ad344d8816074a4a526094e54309c
        return False
