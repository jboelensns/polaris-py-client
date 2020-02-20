#!/usr/bin/env python3
import os
import yaml
from polarisapi import api_client
from polarisapi.api import IpamPrefixApi

from polarisapi.config_helper import ConfigHelper

def main():

    with open("%s/.polaris.yml" % os.environ["HOME"], "r") as f:
        cfg = yaml.load(f)

    host = "http://localhost:8989"
    helper = ConfigHelper(cfg["access_id"], cfg["secret_token"], host=host)

    ipam_client = IpamPrefixApi(api_client.ApiClient(helper.config))
    results = ipam_client.api_v01_ipam_prefix_id_get(232)
    print(results)


if __name__ == '__main__':
    main()
