#!/usr/bin/env python

# File is part of task UC1

import requests
import json
import common_data

# Begin read for each device read in devices_list
with open('data/devices_list.txt') as f:
    devices = f.read().splitlines()

for device in devices:
    print('Reading configuration for ' + device)
    url = "https://" + device + "/restconf/data/Cisco-IOS-XE-native:native/vrf"

    response = requests.get(url, headers=common_data.headers, verify=False)
    common_data.printApiResponse(response)
    data = response.json()
    print('\n================  Print VRF Config  ================\n')
    print('#  VRF\t\t\tRD\t\tRoute-Target'
          '\n----------------------------------------------------------')
    i = 1
    for value in data['Cisco-IOS-XE-native:vrf']['definition']:
        name = value['name']

        try:
            rd = value['rd']
        except:
            rd = ''

        try:
            asn_import = value['route-target']['import'][0]['asn-ip']
            asn_export = value['route-target']['export'][0]['asn-ip']
            asn = 'I: ' + asn_import + ' E: ' + asn_export
        except:
            asn = ''

        print(str(i) + '  ' + name + '\t\t' + rd + '\t' + asn)
        i = i + 1

    print('\n')
