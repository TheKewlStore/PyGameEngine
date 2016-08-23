import attr
import logging

logger = logging.getLogger('root.event')


@attr.s
class Slot(object):
    callback = attr.ib()

    def call(self, args, kwargs):
        self.callback(*args, **kwargs)

    def __str__(self):
        return '{0}({1})'.format(self.__class__.__name__, self.callback.__name__)
