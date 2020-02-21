#!/usr/bin/env python3
import os
import yaml
from polarisgenclient.api_client import ApiClient
from polarisgenclient.api import ArpApi

from polarisgenclient.config_helper import ConfigHelper


def main():

    with open("%s/.polaris.yml" % os.environ["HOME"], "r") as f:
        cfg = yaml.load(f)

    host = "http://localhost:8989"
    helper = ConfigHelper(cfg["access_id"], cfg["secret_token"], host=host)

    client = ArpApi(ApiClient(helper.config))
    print(client.arp_get())


if __name__ == '__main__':
    main()
