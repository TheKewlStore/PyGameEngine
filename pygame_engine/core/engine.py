import attr
import logging
import pygame
import sys

from lib.event.signal import Signal


logger = logging.getLogger('root.engine')
clock = pygame.time.Clock()


@attr.s
class Engine(object):
    fps = attr.ib(default=60)
    _event_signals = attr.ib(init=False, default=attr.Factory(dict), repr=False)

    def register_callback(self, event_type, callback):
        if not event_type in self._event_signals:
            self._event_signals[event_type] = Signal()

        self._event_signals[event_type].connect(callback)

    def run(self):
        pygame.init()

        self.register_callback(pygame.QUIT, self.quit)

        while True:
            elapsed_time = clock.tick(self.fps) / 1000.0

            for event in pygame.event.get():
                if not event.type in self._event_signals:
                    continue

                signal = self._event_signals[event.type]

                logger.debug('Invoking event handlers for {0}'.format(repr(signal)))

                signal.emit(elapsed_time=elapsed_time, **event.dict)

    def quit(self):
        sys.exit(0)
