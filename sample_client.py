#!/usr/bin/env python3
import os
import yaml
from polarisgenclient.api_client import ApiClient
from polarisgenclient.api import IpamPrefixApi

from polarisgenclient.config_helper import ConfigHelper

def main():

    with open("%s/.polaris.yml" % os.environ["HOME"], "r") as f:
        cfg = yaml.load(f)

    host = "http://localhost:8989"
    helper = ConfigHelper(cfg["access_id"], cfg["secret_token"], host=host)

    ipam_client = IpamPrefixApi(ApiClient(helper.config))
    results = ipam_client.api_v01_ipam_prefix_id_get(232)
    print(results)

    ipfilter_client = IpFilterApi(ApiClient(helper.config))
    print(ipfilter_client.api_v01_ipfilter_get("", 1))


if __name__ == '__main__':
    main()
