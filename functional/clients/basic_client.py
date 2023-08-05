import mureq
from mureq import Response


class BClient:

    @staticmethod
    def custom_request(method, url, **kwargs) -> Response:
        response = mureq.request(method, url, **kwargs)
        return response
