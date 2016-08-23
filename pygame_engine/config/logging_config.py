from python_utilities import log_util
from python_utilities import os_util

from pygame_engine.config.config import EngineConfiguration


configuration = EngineConfiguration()


def setup():
    setup_core()
    setup_event()


def setup_core():
    initialize_logger_from_config('root.core.engine')


def setup_event():
    initialize_logger_from_config('root.event')


def initialize_logger_from_config(logger_name):
    logger_enabled = configuration[logger_name + '.logger']['enabled'] == 'True'

    if not logger_enabled:
        return

    filepath = configuration[logger_name + '.logger']['path']
    log_level = configuration[logger_name + '.logger']['level']
    console_output = configuration[logger_name + '.logger']['console'] == 'True'
    debug_color = configuration[logger_name + '.logger']['color_debug']
    info_color = configuration[logger_name + '.logger']['color_info']
    warning_color = configuration[logger_name + '.logger']['color_warning']
    error_color = configuration[logger_name + '.logger']['color_error']
    critical_color = configuration[logger_name + '.logger']['color_critical']
    regex_filter = configuration[logger_name + '.logger']['regex_filter']
    max_size = int(configuration[logger_name + '.logger']['max_size'])
    colors = {'DEBUG': debug_color,
              'INFO': info_color,
              'WARNING': warning_color,
              'ERROR': error_color,
              'CRITICAL': critical_color,
              }

    if not os_util.exists(os_util.directory_name(filepath)):
        os_util.make_directories(os_util.directory_name(filepath))

    log_util.initialize(name=logger_name,
                        filepath=filepath,
                        level=log_level,
                        console_output=console_output,
                        log_colors=colors,
                        regex_filter=regex_filter,
                        max_size=max_size)
