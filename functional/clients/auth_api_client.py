from config import settings
from functional.clients.basic_client import BClient


class AuthClient(BClient):
    __current_user_endpoint = settings.AUTH_API_CURRENT_USER

    def get_user(self, headers):
        response = self.custom_request(
            method="GET",
            url=self.__current_user_endpoint,
            headers=headers
        )
        return response
