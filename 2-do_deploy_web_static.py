#!/usr/bin/python3
""" Fabric script that generates a .tgz archive
from the contents of the web_static folder
sing the function do_pack. """

from fabric.api import *
from datetime import datetime
from os.path import exists

env.user = 'ubuntu'
env.hosts = ['52.23.231.242', '34.229.134.248']
env.key_filename = ['~/.ssh/id_rsa']


def do_pack():
    """
        Generates a .tgz archine from contents of web_static
    """
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = "versions/web_static_{}.tgz".format(date)
    local("mkdir -p versions")
    archive_file = local("tar -czvf {} web_static".format(filename))
    if archive_file:
        return filename
    else:
        return None


def do_deploy(archive_path):
    """
        Distributes an archive to your web servers
        Returns False if archive_path doesnt exist
    """

    if exists(archive_path) is False:
        return False

    else:
        path = '/data/web_static/releases/'
        f_name = archive_path.split("/")[-1]
        f_name_no_ext = f_name.split(".")[0]
        put(archive_path, '/tmp')
        run('mkdir -p {}{}/'.format(path, f_name_no_ext))
        run('tar -xzf /tmp/{} -C {}{}'.format(f_name, path, f_name_no_ext))
        run('rm /tmp/{}'.format(f_name))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, f_name_no_ext))
        run('rm -rf {}{}/web_static'.format(path, f_name_no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, f_name_no_ext))
        run('echo "New version deployed!"')
