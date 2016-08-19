import attr
import logging

from slot import Slot


logger = logging.getLogger('root.lib.event')


@attr.s
class Signal(object):
    name = attr.ib(convert=str)
    _slots = attr.ib(init=False, default=attr.Factory(list))

    def connect(self, callback):
        self._slots.insert(0, Slot(callback))

    def emit(self, *args, **kwargs):
        self.log_event('Event triggered, invoking registered handlers'.format())

        for slot in self._slots:
            self.log_event('Invoking handler {0}'.format(slot))
            self.log_event('    arguments: {0}'.format(args))
            self.log_event('    keyword-arguments: {0}'.format(kwargs))
            slot.call(args, kwargs)

    def log_event(self, message):
        logger.debug('[EVENT-{0}] {1}'.format(self.name, message))
