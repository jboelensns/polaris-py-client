from PKG_NAME.configuration import Configuration
from PKG_NAME.jwt import jwt_header


class ConfigHelper():

    def __init__(self, access_id, secret_token,
                 jwt_func=jwt_header,
                 config=None,
                 header="X-Polaris-Signed",
                 host="https://api.polaris.nskope.net/api/v0.1"):

        self.access_id = access_id
        self.secret_token = secret_token
        self.header = header
        self.host = host
        self.jwt_func = jwt_func

        if config is None:
            self.config = self.build_config()
        else:
            self.config = config

    def build_config(self):
        config = Configuration()
        config.host = self.host
        config.api_key[self.header] = self.get_jwt_str()
        config.refresh_api_key_hook = self.on_refresh_api_key_hook
        config.verify_ssl = False
        return config

    def get_jwt_str(self):
        return self.jwt_func(access_id=self.access_id, secret_token=self.secret_token)

    def on_refresh_api_key_hook(self, config):
        config.api_key[self.header] = self.get_jwt_str()
