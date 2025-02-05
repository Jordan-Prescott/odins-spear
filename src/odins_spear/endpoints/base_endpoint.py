from ..requester import Requester


class BaseEndpoint:
    def __init__(self, logger=None):
        self._requester = Requester.get_instance()
        self._logger = logger
