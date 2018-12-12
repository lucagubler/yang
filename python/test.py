#!/usr/bin/env python

# File is part of task UC4

import json
import requests
import time
import common_data
import sys

# Read arguments
if(len(sys.argv) < 3):
    print('Usage: deploy_bgp_neighbor.py <router-id> <loopback-interface> <remote-asn>')
    quit(2)
r_id = sys.argv[1]
lo_int = sys.argv[2]
r_as = sys.argv[3]

print(r_id + '\n' + lo_int + '\n' + r_as)

with open('data/devices_list.txt') as f:
    devices = f.read().splitlines()

for device in devices:
    print('Starting configuration for ' + device)
    # Add BGP Neighbor
    print('\n===============  Deploy BGP Neighbor  ==============\n')

    url = "https://" + device + "/restconf/data/Cisco-IOS-XE-native:native/router/bgp=65000/neighbor"

    with open('data/uc4_bgp_neighborship.json') as jsonfile:
        payload = json.load(jsonfile)
    payload['Cisco-IOS-XE-bgp:neighbor'][0]['id'] = r_id
    payload['Cisco-IOS-XE-bgp:neighbor'][0]['remote-as'] = r_as
    payload['Cisco-IOS-XE-bgp:neighbor'][0]['update-source']['Loopback'] = lo_int
    print(payload)