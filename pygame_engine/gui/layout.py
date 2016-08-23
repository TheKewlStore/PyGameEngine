""" Module docstring.

    Author: Ian Davis
"""
import attr

from pygame_engine.data import Point


@attr.s
class Layout(object):
    """ Represent a layout of widgets to manage position calculation automatically.
    """
    name = attr.ib()
    width = attr.ib()
    height = attr.ib()
    _widgets = attr.ib(default=[], init=False, repr=False)

    def add_widget(self, widget):
        """ Add the given widget to the end of the layout.

            :param widget: The widget to add.
            :return: None
        """
        self.widgets.append(widget)

    def get_origin(self, widget):
        """ Calculate the origin for a given widget in the layout.

            :param widget: The PGEWidget to calculate the origin for.
            :return: The point of origin for this widget.
            :rtype: Point
        """
        raise NotImplementedError('get_rect must be implemented by subclasses')


@attr.s
class VerticalLayout(Layout):
    """ Represent a layout of widgets spaced vertically across the parent widget.
    """

    def add_widget(self, widget):
        """ Add the given widget to the end of the layout and recalculate all widget's sizes to fit in the layout.

            :param widget: The widget to add.
            :return: None
        """
        self.widgets.append(widget)
        self._redistribute_widgets()

    def get_origin(self, widget):
        """ Calculate the origin for a given widget in the layout.

            :param widget: The PGEWidget to calculate the origin for.
            :return: The point of origin for this widget.
            :rtype: Point
            :raise ValueError: If the widget given is not in the layout.
        """
        if widget not in self.widgets:
            raise ValueError('Widget not in layout!')

        widget_index = self.widgets.index(widget)
        origin = Point(0, 0)

        for previous_widget in self.widgets[0:widget_index]:
            origin.y += previous_widget.height

        return origin

    def _redistribute_widgets(self):
        """ Redistribute the width and height of all widgets in the layout to properly fit the layout size.

            :return: None
        """
        widget_width = self.width
        widget_height = self.height / len(self.widgets)

        for widget in self._widgets:
            widget.width = widget_width
            widget.height = widget_height


@attr.s
class HorizontalLayout(Layout):
    """ Represent a layout of widgets spaced horizontally across the parent widget.
    """

    def add_widget(self, widget):
        """ Add the given widget to the end of the layout and recalculate all widget's sizes to fit in the layout.

            :param widget: The widget to add.
            :return: None
        """
        self._widgets.append(widget)
        self._redistribute_widgets()

    def get_origin(self, widget):
        """ Calculate the origin for a given widget in the layout.

            :param widget: The PGEWidget to calculate the origin for.
            :return: The point of origin for this widget.
            :rtype: Point
            :raise ValueError: If the widget given is not in the layout.
        """
        if widget not in self.widgets:
            raise ValueError('Widget not in layout!')

        widget_index = self.widgets.index(widget)
        origin = Point(0, 0)

        for previous_widget in self.widgets[0:widget_index]:
            origin.x += previous_widget.width

        return origin

    def _redistribute_widgets(self):
        """ Redistribute the width and height of all widgets in the layout to properly fit the layout size.

            :return: None
        """
        widget_width = self.width / len(self.widgets)
        widget_height = self.height

        for widget in self.widgets:
            widget.width = widget_width
            widget.height = widget_height
