#!/usr/bin/env python

# File is part of task UC3

import json
import requests
import common_data

with open('devices_list.txt') as f:
    devices = f.read().splitlines()

for device in devices:
    print('Starting configuration for ' + device)
    # Remove VRF from BGP
    print('\n===============  Delete VRF Config  ===============\n')
    url = "https://" + device + "/restconf/data/Cisco-IOS-XE-native:native/router/bgp=65000/address-family/with-vrf/ipv4=unicast/vrf=myVRF"
    
    time.sleep(7)
    response = requests.request("DELETE", url, headers=common_data.headers, verify=False)

    common_data.printApiResponse(response)

    # Delete VRF itself
    url = "https://" + device + "/restconf/data/Cisco-IOS-XE-native:native/vrf/definition=myVRF"

    time.sleep(7)
    response = requests.request("DELETE", url, headers=common_data.headers, verify=False)

    common_data.printApiResponse(response)
