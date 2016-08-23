""" Define the Engine, which is the main handler of games created with PyGameEngine.

    Author: Ian Davis
"""
import logging
import sys

import pygame

from pygame_engine.event import Signal
from pygame_engine.config import logging_config

logging_config.setup()
logger = logging.getLogger('root.core.engine')
clock = pygame.time.Clock()


class Engine(object):
    """ Main manager of the game engine event loop,
        Engine is the entry point into a game application.
    """
    _fps = 60
    _event_signals = {}
    _instance = None
    _event_loop_running = False

    def __init__(self, fps=60):
        """ Engine initializer.

            :param fps: The frames per second that the application will use,
                this will limit the processing speed of the event loop.
            :raise RuntimeError: If an Engine is instantiated when one already exists.
        """
        if Engine._instance:
            raise RuntimeError('An engine has already been defined, use Engine.instance instead')

        self._fps = fps
        Engine._instance = self

    @classmethod
    def instance(cls):
        """ Get the shared engine instance that has already been initialized.

            :return: Engine instance.
        """
        return cls._instance

    def register_callback(self, event_type, callback):
        """ Register a new slot callback to be fired when the given event is triggered in the event loop.

            :param event_type: The event type to connect to.
            :param callback: The callback to invoke when the event is triggered.
            :return: None
        """

        if event_type not in self._event_signals:
            self._event_signals[event_type] = Signal(event_type)

        self._event_signals[event_type].connect(callback)

    def run(self):
        """ Run the event loop and start the game processing.

            :raise RuntimeError: If run is called when the event loop is already running.
            :return: None
        """
        if Engine._event_loop_running:
            raise RuntimeError("The engine's event loop is already running!")

        Engine._event_loop_running = True
        logger.info('initializing engine')

        pygame.init()

        self.register_callback(pygame.QUIT, self.quit)

        logger.info('engine initialized, starting event loop')
        logger.info('event loop started')

        if 'startup' in self._event_signals:
            self._event_signals['startup'].emit()

        while True:
            elapsed_time = clock.tick(self._fps) / 1000.0

            for event in pygame.event.get():
                if event.type not in self._event_signals:
                    continue

                signal = self._event_signals[event.type]
                signal.emit(elapsed_time=elapsed_time, **event.dict)

            if 'paint' in self._event_signals:
                signal = self._event_signals['paint']
                signal.emit()

    @staticmethod
    def quit(*args, **kwargs):
        """ Builtin slot handler to shutdown the engine when pygame.QUIT is received.

        :param args: Any var-args passed to the slot from the event.
        :param kwargs: Any kwargs passed to the slot from the event.
        :return: None
        """
        logger.info('event loop stopped, closing engine.')
        sys.exit(0)
