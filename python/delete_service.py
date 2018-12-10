#!/usr/bin/env python

# File is part of task UC3

import json
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

headers = {
    'Accept': "application/yang-data+json",
    'Content-Type': "application/yang-data+json",
    'Authorization': "Basic aW5zOmluc0BsYWI=",
    }

with open('devices_list.txt') as f:
    devices = f.read().splitlines()

for device in devices:
    print('Starting configuration for ' + device)
    # Remove VRF from BGP
    print('\n\n===============  Delete VRF Config  ===============\n\n')
    url = "https://" + device + "/restconf/data/Cisco-IOS-XE-native:native/router/bgp=65000/address-family/with-vrf/ipv4=unicast/vrf=myVRF"

    response = requests.request("DELETE", url, headers=headers, verify=False)
    print('Response OK if there is no output below this line: \n' + response.text)

    # Delete VRF itself
    url = "https://" + device + "/restconf/data/Cisco-IOS-XE-native:native/vrf/definition=myVRF"

    response = requests.request("DELETE", url, headers=headers, verify=False)
    print('Response OK if there is no output below this line: \n' + response.text)