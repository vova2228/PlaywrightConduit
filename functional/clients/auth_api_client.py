from config import settings
from functional.clients.basic_client import BClient


class AuthClient(BClient):
    __current_user_endpoint = settings.AUTH_API_CURRENT_USER

    def get_user(self):
        response = self.custom_request("GET", self.__current_user_endpoint)
        return response
