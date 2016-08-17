from python_utils.config_util import Configuration
from python_utils import os_util

from pygame_engine.core import environment


def logging_default_section(logger_name):
    default_filepath = os_util.make_path(environment.project_root(), 'logs', '{0}.txt'.format(logger_name.replace('.', '-')))

    return {'path': default_filepath,
            'level': 'WARNING',
            'console': 'False',
            'color_debug': 'cyan',
            'color_info': 'green',
            'color_warning': 'yellow',
            'color_error': 'red',
            'color_critical': 'red,bg_white'
           }


class EngineConfiguration(Configuration):
    def __init__(self):
        default_sections = {'root.core.engine.logger': logging_default_section('root.core.engine'),
                            'root.lib.event.logger': logging_default_section('root.lib.event'),
                           }

        file_path = os_util.make_path(environment.project_root(), 'engine.ini')

        super(EngineConfiguration, self).__init__(file_path, default_sections=default_sections)
