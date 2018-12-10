#!/usr/bin/env python

# File is part of task UC4

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
    print('\n\n===============  Deply BGP Neighbor  ==============\n\n')

    url = "https://" + device + "/restconf/data/Cisco-IOS-XE-native:native/router/bgp=65000"



    with open('uc2_vrf_conf.json') as jsonfile:
        payload = json.load(jsonfile)
    response = requests.request("PATCH", url, json=payload, headers=headers, verify=False)

    print('Response OK if there is no output below this line: \n' + response.text)