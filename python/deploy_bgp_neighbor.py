#!/usr/bin/env python

# File is part of task UC4

import json
import requests
import time
import common_data

with open('devices_list.txt') as f:
    devices = f.read().splitlines()

for device in devices:
    print('Starting configuration for ' + device)
    print('\n===============  Deploy BGP Neighbor  ==============\n')

    url = "https://" + device + "/restconf/data/Cisco-IOS-XE-native:native/router/bgp=65000"

    with open('uc2_vrf_conf.json') as jsonfile:
        payload = json.load(jsonfile)
    time.sleep(7)
    response = requests.request("PATCH", url, json=payload, headers=common_data.headers, verify=False)

    common_data.printApiResponse(response)