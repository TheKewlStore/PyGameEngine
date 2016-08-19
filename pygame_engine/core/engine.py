import logging
import pygame
import sys

from pygame_engine.lib import logging_config
from pygame_engine.lib.event.signal import Signal


logging_config.setup()
logger = logging.getLogger('root.core.engine')
clock = pygame.time.Clock()


class Engine(object):
    _fps = 60
    _event_signals = {}
    _instance = None

    def __init__(self, fps=60):
        self._fps = fps
        Engine._instance = self

    @classmethod
    def instance(cls):
        return cls._instance

    def register_callback(self, event_type, callback):
        if event_type not in self._event_signals:
            self._event_signals[event_type] = Signal(event_type)

        self._event_signals[event_type].connect(callback)

    def run(self):
        logger.debug('initializing engine')

        pygame.init()

        self.register_callback(pygame.QUIT, self.quit)

        logger.debug('engine initialized, starting event loop')
        logger.debug('event loop started')

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
        logger.debug('event loop stopped, closing engine.')
        sys.exit(0)
