import attr
import logging

from slot import Slot


logger = logging.getLogger('root.lib.event')


@attr.s
class Signal(object):
    _slots = attr.ib(init=False, default=attr.Factory(list))

    def connect(self, callback):
        self._slots.insert(0, Slot(callback))

    def emit(self, *args, **kwargs):
        for slot in self._slots:
            logger.debug('Invoking slot {0} for signal {1}'.format(slot, self))

            slot.call(args, kwargs)
