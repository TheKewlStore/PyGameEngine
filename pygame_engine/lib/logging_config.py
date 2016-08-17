from python_utils import log_util
from python_utils import os_util

from pygame_engine.lib.config import EngineConfiguration


configuration = EngineConfiguration()


def setup():
    setup_root_core()


def setup_root_core():
    initialize_logger_from_config('root.core.engine')
    initialize_logger_from_config('root.lib.event')


def initialize_logger_from_config(logger_name):
    filepath = configuration[logger_name + '.logger']['path']
    log_level = configuration[logger_name + '.logger']['level']
    console_output = configuration[logger_name + '.logger']['console']
    debug_color = configuration[logger_name + '.logger']['color_debug']
    info_color = configuration[logger_name + '.logger']['color_info']
    warning_color = configuration[logger_name + '.logger']['color_warning']
    error_color = configuration[logger_name + '.logger']['color_error']
    critical_color = configuration[logger_name + '.logger']['color_critical']
    colors = {'DEBUG': debug_color,
              'INFO': info_color,
              'WARNING': warning_color,
              'ERROR': error_color,
              'CRITICAL': critical_color,
             }

    if not os_util.exists(os_util.directory_name(filepath)):
        os_util.make_directories(os_util.directory_name(filepath))

    log_util.initialize(name=logger_name, filepath=filepath, level=log_level, console_output=console_output, log_colors=colors)
