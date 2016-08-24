from collections import OrderedDict as OrderedDictionary

from python_utilities.config_util import Configuration
from python_utilities import os_util

from pygame_engine.core import environment


def logging_default_section(logger_name):
    """ Create a new OrderedDictionary representing a configuration section for a logger with the given name.

        :param logger_name: The name of the logger to create a configuration section for.
        :return: An OrderedDictionary of the configuration section created.
    """
    default_file_path = os_util.make_path(environment.project_root(), 'logs', '{0}.txt'.format(logger_name.replace('.', '-')))

    section = OrderedDictionary()
    section['enabled'] = 'True'
    section['path'] = default_file_path
    section['level'] = 'WARNING'
    section['console'] = 'False'
    section['regex_filter'] = '.*'
    section['max_size'] = '100'
    section['color_debug'] = 'cyan'
    section['color_info'] = 'green'
    section['color_warning'] = 'yellow'
    section['color_error'] = 'red'
    section['color_critical'] = 'red,bg_white'

    return section


class EngineConfiguration(Configuration):
    """ Represent the Configuration manager for the PyGameEngine.
    """
    def __init__(self):
        default_sections = OrderedDictionary()
        default_sections['root.core.engine.logger'] = logging_default_section('root.core.engine')
        default_sections['root.event.logger'] = logging_default_section('root.event')

        file_path = os_util.make_path(environment.project_root(), 'engine.ini')

        super(EngineConfiguration, self).__init__(file_path, default_sections=default_sections)
