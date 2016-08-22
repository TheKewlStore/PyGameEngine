from pygame_engine.core.engine import Engine
from pygame_engine.core.display import Display
from pygame_engine.lib.gui.widget import PGEWidget
from pygame_engine.lib.data.size import Size


def startup():
    """ Event handler called when the PyGameEngine starts up.

        Used to create a display and test any dynamic runtime functionality.
    """
    main_widget = PGEWidget(Size(640, 480))
    display = Display(Size(640, 480), main_widget=main_widget)


if __name__ == '__main__':
    engine = Engine()
    engine.register_callback('startup', startup)
    engine.run()
