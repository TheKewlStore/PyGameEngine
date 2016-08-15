import attr
import logging


logger = logging.getLogger('root.lib.event')


@attr.s
class Slot(object):
    callback = attr.ib()

    def call(self, args, kwargs):
        logger.debug('Invoking {0}\n    arguments: {1}\n    keyword-arguments: {2}'.format(self.callback, args, kwargs))
        self.callback(args, kwargs)
