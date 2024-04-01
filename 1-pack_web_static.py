#!/usr/bin/python3
""" Fabric script that generates a .tgz archive
from the contents of the web_static folder
sing the function do_pack. """

from fabric.api import local
from datetime import datetime


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
