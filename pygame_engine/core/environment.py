""" Define functions to manage and manipulate the python path for this project.
"""
from python_utilities import os_util


# TODO: Consider options for phasing this out.


def project_root():
    """ Return the root path of the project.

        :return: None
    """
    return os_util.directory_name(os_util.directory_name(os_util.module_path(__file__)))


def setup():
    """ Add the project root to the python path.

        :return: None
    """
    os_util.add_python_path(project_root())
