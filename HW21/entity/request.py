from typing import Dict

from entity.abstact_storage import AbstractStorage
from exceptions import InvalidRequest, InvalidStorageName


class Request:

    def __init__(self, request: str, storages: Dict[str, AbstractStorage]):

        splitted_request = request.lower().split(' ')
        if len(splitted_request) != 7:
            raise InvalidRequest

        self.amount = int(splitted_request[1])
        self.product = int(splitted_request[2])
        self.departure = int(splitted_request[4])
        self.destination = int(splitted_request[6])

        if self.departure not in storages or self.destination not in storages:
            raise InvalidStorageName
