from typing import Dict

from entity.abstact_storage import AbstractStorage
from entity.request import Request


class Courier:

    def __init__(self, request: Request, storages: Dict[str, AbstractStorage]):
        self.__request = request

        if self.__request.departure in storages:
            self.__from = storages[self.__request.departure]

        if self__request.destination in storages:
            self.__to = storages[self__request.destination]