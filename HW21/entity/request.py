class Request:

    def __init__(self, request: str):

        splitted_request = request.lower().split(' ')
        if len(splitted_request) != 7:
            raise InvalidRequest

        self.amount = int(splitted_request[1])
        self.product = int(splitted_request[2])
        self.departure = int(splitted_request[4])
        self.destination = int(splitted_request[6])
