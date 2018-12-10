#!/usr/bin/env python

# File is part of task UC2

import json
import requests
import time
import common_data


with open('devices_list.txt') as f:
    devices = f.read().splitlines()

for device in devices:
    print('Starting configuration for ' + device)
    # First deploy VRF
    print('\n===============  Deploy VRF Config  ===============\n')
    
    url = "https://" + device + "/restconf/data/Cisco-IOS-XE-native:native/vrf"

    with open('uc2_vrf_conf.json') as jsonfile:
        payload = json.load(jsonfile)
    time.sleep(7)
    response = requests.request("PATCH", url, json=payload, headers=common_data.headers, verify=False)

    common_data.printApiResponse(response)

    # Secondly deploy BGP configuration for VRF
    print('\n===============  Deploy BGP Config  ===============\n')

    url = "https://" + device + "/restconf/data/Cisco-IOS-XE-native:native/router/bgp=65000/address-family/with-vrf/ipv4=unicast"

    with open('uc2_bgp_conf.json') as jsonfile:
        payload = json.load(jsonfile)

    time.sleep(7)
    response = requests.request("PATCH", url, json=payload, headers=common_data.headers, verify=False)

    common_data.printApiResponse(response)