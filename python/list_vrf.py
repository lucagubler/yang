#!/usr/bin/env python

# File is part of task UC1

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
    url = "https://" + device + "/restconf/data/Cisco-IOS-XE-native:native/vrf"


    response = requests.get(url, headers=headers, verify=False)
    data = response.json()
    print('\n\n================  Print VRF Config  ================\n\n')
    print('#\tVRF Name\n---------------------------')
    i = 1
    for value in data['Cisco-IOS-XE-native:vrf']['definition']:
        name = value['name']
        
        print(str(i) + '\t' + name)
        i = i + 1
