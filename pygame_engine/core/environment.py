from python_utils import os_util


def project_root():
    return os_util.directory_name(os_util.directory_name(os_util.module_path(__file__)))


def setup():
    os_util.add_python_path(project_root())

