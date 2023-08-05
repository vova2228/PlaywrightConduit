import env


class Settings:
    BASE_URL = env.WEB_URL['base_url']
    LOGIN_URL = env.WEB_URL['login_url']
    SIGN_UP_URL = env.WEB_URL['sign_up_url']

    AUTH_API_CURRENT_USER = env.AUTH_API['get_user']
