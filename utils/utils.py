from time import sleep


class Utils:

    @staticmethod
    def get_user_token_from_local_storage(page) -> str:
        try:
            return page.page.context.storage_state()['origins'][0]['localStorage'][0]['value']
        except IndexError:
            sleep(2)
            return page.page.context.storage_state()['origins'][0]['localStorage'][0]['value']
