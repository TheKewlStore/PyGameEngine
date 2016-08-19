import pygame

from pygame_engine.core.engine import Engine
from pygame_engine.lib.data import color


class Display(object):
    def __init__(self, size):
        self._screen = pygame.display.set_mode(size)

        self._register_default_callbacks()

    def paint(self):
        self._screen.fill(color.BLACK)

    def _register_default_callbacks(self):
        Engine.instance().register_callback('paint', self.paint)
