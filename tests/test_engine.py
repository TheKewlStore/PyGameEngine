from pygame_engine.data import color
from pygame_engine.gui.widget import PGERootWidget

from pygame_engine.core.display import Display
from pygame_engine.core.engine import Engine
from pygame_engine.data.size import Size
from pygame_engine.gui.label import Label


class TestWidget(PGERootWidget):
    def paint(self):
        self.surface.fill(color.RED)


def startup():
    """ Event handler called when the PyGameEngine starts up.

        Used to create a display and test any dynamic runtime functionality.
    """
    main_widget = TestWidget(Size(640, 480))
    label = Label('Hello World!', Size(300, 100))
    display = Display(Size(640, 480), main_widget=main_widget)


if __name__ == '__main__':
    engine = Engine()
    engine.register_callback('startup', startup)
    engine.run()
