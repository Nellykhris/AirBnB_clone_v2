#!/usr/bin/python3
<<<<<<< HEAD
"""create archive module"""
from os.path import isdir
=======
<<<<<<< HEAD
"""create archive module"""
from os.path import isdir
=======
""" Fabric script """
>>>>>>> 1aa7c1466d9987c8ee2e2d156b5bb710c6c822b1
>>>>>>> 830f3165d26ad344d8816074a4a526094e54309c
from fabric.api import local
from datetime import datetime


def do_pack():
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 830f3165d26ad344d8816074a4a526094e54309c
    """function to zip files"""
    try:
        new_date = datetime.now()
        new_date = new_date.strftime('%Y%m%d%H%M%S')
        archive = f"versions/web_static_{new_date}.tgz"
        if isdir('versions') is False:
            local('mkdir versions')
        print(f"Packing web_static to {archive}")
        var = local(f'tar -cvzf {archive} web_static')
        return archive
<<<<<<< HEAD
        except Exception:
            return None
=======
    except Exception:
=======
    """ Generates a .tgz file from the contents of 'web_static' folder"""
    now = datetime.now()
    local('mkdir -p versions')
    result = local('tar -cvzf versions/web_static_{}.tgz ./web_static/'.format(
        now.strftime('%Y%m%d%H%M%S')))
    if result.succeeded:
        return 'versions/web_static_{}.tgz web_static/'.format(
                now.strftime('%Y%m%d%H%M%S'))
    else:
>>>>>>> 1aa7c1466d9987c8ee2e2d156b5bb710c6c822b1
        return None
>>>>>>> 830f3165d26ad344d8816074a4a526094e54309c
