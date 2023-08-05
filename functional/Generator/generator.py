import random
import string

letters = string.ascii_lowercase
digits = string.digits


class TestDataGenerator:

    def generate_user_data(self, length=8):
        email = self.generate_email(length)
        password = self.generate_password(length)
        username = self.generate_username(length)
        return email, password, username

    @classmethod
    def generate_email(cls, length=8):
        username = ''.join(random.choices(letters, k=length))
        domain = ''.join(random.choices(letters, k=length))
        email = f"{username}@{domain}.com"
        return email

    @classmethod
    def generate_password(cls, length=8):
        password = ''.join(random.choices(digits + letters, k=length))
        return password

    @classmethod
    def generate_username(cls, length=8):
        username = ''.join(random.choices(letters, k=length))
        return username
