from mureq import Response
from functional.clients.auth_api_client import AuthClient


class AuthAPI:
    __client = AuthClient()

    # __deserializer = Deserializer()

    @classmethod
    def get_current_user(cls, token) -> Response:
        print("\nGetting the current user...")
        headers = {"Authorization": f'Token {token}'}
        response = cls.__client.get_user()
        return response
