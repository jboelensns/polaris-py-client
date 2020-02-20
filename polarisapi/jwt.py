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
