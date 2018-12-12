#!/usr/bin/env python

# File is part of task UC1

import requests, json
import common_data



with open('devices_list.txt') as f:
    devices = f.read().splitlines()

for device in devices:
    print('Reading configuration for ' + device)
    url = "https://" + device + "/restconf/data/Cisco-IOS-XE-native:native/vrf"

    response = requests.get(url, headers=common_data.headers, verify=False)
    common_data.printApiResponse(response)
    data = response.json()
    print('\n================  Print VRF Config  ================\n')
    print('#\tVRF Name\n---------------------------')
    i = 1
    for value in data['Cisco-IOS-XE-native:vrf']['definition']:
        name = value['name']
        
        print(str(i) + '\t' + name)
        i = i + 1
    
    print('\n')