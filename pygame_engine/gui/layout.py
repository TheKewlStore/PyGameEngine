""" Module docstring.

    Author: Ian Davis
"""
import attr
import logging

from pygame_engine.data import Point
from pygame_engine.data import Size


logger = logging.getLogger('root.gui.layout')


@attr.s
class Layout(object):
    """ Represent a layout of widgets to manage position calculation automatically.
    """
    name = attr.ib()
    width = attr.ib()
    height = attr.ib()
    parent = attr.ib()
    widgets = attr.ib(default=attr.Factory(list), init=False, repr=False)

    def add_widget(self, widget):
        """ Add the given widget to the end of the layout.

            :param widget: The widget to add.
            :return: None
        """
        logger.debug('Adding widget {0} to layout'.format(widget))
        widget.surface = self.parent.surface.subsurface(widget.rect)
        self.widgets.append(widget)
        self._redistribute_widgets()
        self._update_widget_surfaces()
        self._invalidate_widgets()

    def get_origin(self, widget):
        """ Calculate the origin for a given widget in the layout.

            :param widget: The PGEWidget to calculate the origin for.
            :return: The point of origin for this widget.
            :rtype: Point
        """
        raise NotImplementedError('get_rect must be implemented by subclasses')

    def paint_widgets(self):
        for widget in self.widgets:
            widget.paint()

    def _invalidate_widgets(self):
        """ Reset all widgets display by signifying that they all need repainted.
        """
        for widget in self.widgets:
            widget.needs_repaint = True

    def _redistribute_widgets(self):
        """ Redistribute the width and height of all widgets in the layout to properly fit the layout size.

            :return: None
        """
        raise NotImplementedError('Abstract method')

    def _update_widget_surfaces(self):
        """ Called after a new widget is added to the layout, this method updates the surface rects for all widgets to reflect any size changes that occurred.

            :return: None
        """
        for widget in self.widgets:
            logger.debug('Updating surface geometry for widget {0}'.format(widget))
            logger.debug('    {0}'.format(widget.rect))
            widget.surface = self.parent.surface.subsurface(widget.rect)

    def __str__(self):
        return '{0}[width={1}, height={2}]'.format(self.name, self.width, self.height)

@attr.s
class VerticalLayout(Layout):
    """ Represent a layout of widgets spaced vertically across the parent widget.
    """
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
            origin.y += previous_widget.size.height

        return origin

    def _redistribute_widgets(self):
        """ Redistribute the width and height of all widgets in the layout to properly fit the layout size.

            :return: None
        """
        widget_width = self.width
        widget_height = self.height / len(self.widgets)
        widget_size = Size(widget_width, widget_height)

        for widget in self.widgets:
            widget.size = widget_size
            widget.origin = self.get_origin(widget)


@attr.s
class HorizontalLayout(Layout):
    """ Represent a layout of widgets spaced horizontally across the parent widget.
    """
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
        widget_size = Size(widget_width, widget_height)

        for widget in self.widgets:
            widget.size = widget_size
            widget.origin = self.get_origin(widget)
