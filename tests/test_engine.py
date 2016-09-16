from pygame_engine.data import color
from pygame_engine.gui.widget import PGEWidget

from pygame_engine.core.display import Display
from pygame_engine.core.engine import Engine
from pygame_engine.data.point import Point
from pygame_engine.data.size import Size
from pygame_engine.gui.label import Label


class TestWidget(PGEWidget):
    def paint(self):
        self.surface.fill(color.WHITE)
        super(TestWidget, self).paint()


def startup():
    """ Event handler called when the PyGameEngine starts up.

        Used to create a display and test any dynamic runtime functionality.
    """
    display = Display(Size(1280, 720))
    main_widget = TestWidget('root', Size(853, 480))
    main_widget.origin = Point(213, 120)

    display.main_widget = main_widget

    top_widget = PGEWidget('top', Size(320, 240), parent=main_widget)
    label = Label('hello_label', 'Hello World!', Size(300, 100), font_size=25, parent=top_widget)

    top_spacer = PGEWidget('top_spacer', Size(300, 50), parent=main_widget)
    bottom_spacer = PGEWidget('bottom_spacer', Size(300, 50), parent=main_widget)

    main_widget.layout.add_widget(top_widget)

    top_widget.layout.add_widget(top_spacer)
    top_widget.layout.add_widget(label)
    top_widget.layout.add_widget(bottom_spacer)


if __name__ == '__main__':
    engine = Engine()
    engine.register_callback('startup', startup)
    engine.run()
