#!/usr/bin/env python3
import json
import yaml
from polarisapi import api_client
from polarisapi import configuration
from polarisapi.api import PopApi, IpamPrefixApi

import base64
import datetime
import jwt
import logging
import os
import pytz

DEFAULT_ALG = 'HS256'
DEFAULT_NONCE_LEN = 16
DEFAULT_ENV_ACCESS_ID = 'POLARIS_ACCESS_ID'
DEFAULT_ENV_SECRET_TOKEN = 'POLARIS_SECRET_TOKEN'

LOG = logging.getLogger(__name__)


def jwt_header(access_id=None, secret_token=None, alg=DEFAULT_ALG,
               nonce_len=DEFAULT_NONCE_LEN, env_access_id=DEFAULT_ENV_ACCESS_ID,
               env_secret_token=DEFAULT_ENV_SECRET_TOKEN, use_env=False):
    """
    jwt_header
    :param access_id: string (public key)
    :param secret_token: string to be HMAC+SHA256d (private key)
    :param nonce_len: int length of generated nonce
    :param env_access_id: string variable for access_id in environment
    :param env_secret_token: string variable for secret_token in environment
    :param use_env: bool: whether to check environment on missing pub/priv key
    """
    try:
        if not access_id and not secret_token and use_env is True:
            access_id = os.environ.get(env_access_id, None)
            secret_token = os.environ.get(env_secret_token, None)
        if not access_id or not secret_token:
            LOG.error('missing access_id/secret_token')
            return None

        nonce = base64.b64encode(os.urandom(nonce_len)).decode('utf-8')
        ts = datetime.datetime.now(pytz.utc).isoformat()
        p = {
            'nonce': nonce,
            'ts': ts,
        }
        hdr = {
            'kid': access_id,
        }
        hdr_str = jwt.encode(p, secret_token, headers=hdr, algorithm=alg)
        return hdr_str.decode('utf-8')
    except Exception as e:
        LOG.error('exception=%s', repr(e))
        return None


class JwtHelper():

    def __init__(self, access_id=None, secret_token=None, header="X-Polaris-Signed",
                 jwt_func=None, config=None):

        self.access_id = access_id
        self.secret_token = secret_token
        self.header = header
        self.jwt_func = jwt_func
        self.config = config

    def get_config(self):
        if self.config is not None:
            return self.config

        config = configuration.Configuration()
        config.host = "https://api.polaris.nskope.net/api/v0.1"
        config.api_key[self.header] = self.get_jwt_str()
        config.refresh_api_key_hook = self.on_refresh_api_key_hook
        config.verify_ssl = False
        self.config = config

        return config

    def get_jwt_str(self):
        return self.jwt_func(access_id=self.access_id, secret_token=self.secret_token)

    def on_refresh_api_key_hook(self, configuration):
        if self.jwt_func:
            configuration.api_key[self.header] = self.get_jwt_str()


def main():
    with open("/home/jboelens/.polaris.yml", "r") as f:
        polaris_cfg = yaml.load(f)

    access_id = polaris_cfg["access_id"]
    secret_token = polaris_cfg["secret_token"]
    helper = JwtHelper(access_id=access_id, secret_token=secret_token, jwt_func=jwt_header)

    config = configuration.Configuration()
    config.host = "https://api.polaris.nskope.net"
    config.host = "http://localhost:8989"
    #config.host = "https://api.polaris.nskope.net/api/v0.1"
    config.api_key[helper.header] = helper.get_jwt_str()
    config.refresh_api_key_hook = helper.on_refresh_api_key_hook
    config.verify_ssl = False

    ipam_client = IpamPrefixApi(api_client.ApiClient(config))
    results = ipam_client.api_v01_ipam_prefix_id_get(232)
    print(results)
    # for result in results:
    #     json_str = json.dumps(result.to_dict())
    #     print(json_str)
    #     break


if __name__ == '__main__':
    main()
