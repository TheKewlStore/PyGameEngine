from python_utilities import os_util


# TODO: Consider options for phasing this out.
# TODO: Basic documentation.


def project_root():
    return os_util.directory_name(os_util.directory_name(os_util.module_path(__file__)))


def setup():
    os_util.add_python_path(project_root())
