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

    url = "https://" + device + "/restconf/data/Cisco-IOS-XE-native:native/router/bgp=65000/neighbor"

    with open('uc4_bgp_neighborship.json') as jsonfile:
        payload = json.load(jsonfile)
    print(payload)
    time.sleep(7)
    response = requests.request("PATCH", url, json=payload, headers=common_data.headers, verify=False)

    common_data.printApiResponse(response)

    print('\n===============  Add VPNv* Configuration  ==============\n')
    # First create the vpnv4 configuration
    url = "https://" + device + "restconf/data/Cisco-IOS-XE-native:native/router/bgp=65000/address-family/no-vrf/vpnv4=unicast/vpnv4-unicast/neighbor"

    with open('uc4_bgp_neighborship_vpn.json') as jsonfile:
        payload = json.load(jsonfile)
    time.sleep(7)
    response = requests.request("PATCH", url, json=payload, headers=common_data.headers, verify=False)

    common_data.printApiResponse(response)
    # Repeat the same json source for vpnv6 configuration
    url = "https://" + device + "restconf/data/Cisco-IOS-XE-native:native/router/bgp=65000/address-family/no-vrf/vpnv4=unicast/vpnv6-unicast/neighbor"
    time.sleep(7)
    response = requests.request("PATCH", url, json=payload, headers=common_data.headers, verify=False)
