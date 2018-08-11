from abc import ABCMeta, abstractmethod


class Pub(object):
    __metaclass__ = ABCMeta

    def __init__(self, data):
        self.data = data

    @abstractmethod
    def send(self):
        raise NotImplementedError(
            'Pub subclass must override send() method')
