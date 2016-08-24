from pygame_engine.data import color
from pygame_engine.gui.widget import PGERootWidget

from pygame_engine.core.display import Display
from pygame_engine.core.engine import Engine
from pygame_engine.data.size import Size
from pygame_engine.gui.label import Label


class TestWidget(PGERootWidget):
    def paint(self):
        self.surface.fill(color.WHITE)
        super(TestWidget, self).paint()


def startup():
    """ Event handler called when the PyGameEngine starts up.

        Used to create a display and test any dynamic runtime functionality.
    """
    main_widget = TestWidget(Size(640, 480))
    display = Display(Size(640, 480), main_widget=main_widget)
    label = Label('Hello World!', Size(640, 100), font_size=25)
    main_widget.layout.add_widget(label)


if __name__ == '__main__':
    engine = Engine()
    engine.register_callback('startup', startup)
    engine.run()
