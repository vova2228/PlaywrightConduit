from functional.clients.auth_api_client import AuthClient
from models.deserializer import deserialize
from models.user import User


class AuthAPI:

    @classmethod
    def get_current_user(cls, token) -> User | None:
        print("\nGetting the current user by token...")

        headers = {"Authorization": f'Token {token}'}
        response = AuthClient().get_user(headers)
        try:
            current_user = deserialize(response.json()['user'], User)
            print("User received\n")
            return current_user
        except KeyError:
            print(f"User was not received. Status code = {response.status_code} \n")
            return None
