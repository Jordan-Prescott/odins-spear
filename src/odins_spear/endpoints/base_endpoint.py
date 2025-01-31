from ..requester import Requester
from ..logger import Logger


class BaseEndpoint:
    def __init__(self):
        self._requester = Requester.get_instance()
        self._logger = Logger.get_instance()
