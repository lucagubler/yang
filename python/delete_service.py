#!/usr/bin/env python

# File is part of task UC3

import json
import requests
import time
import common_data
import sys
import getopt

name = ''

with open('devices_list.txt') as f:
    devices = f.read().splitlines()

try:
    opts, args = getopt.getopt(argv, "hn:", ["name="])
except getopt.GetoptError:
    print 'usage: delete_service.py -n <name>'
    sys.exit(2)
for opt, arg in opts:
    if opt == '-h':
        print 'usage: delete_service.py -n <name>'
        sys.exit()
    elif opt in ("-n", "--name"):
        name = arg

for device in devices:
    print('Starting configuration for ' + device)
    # Remove VRF from BGP
    print('\n===============  Delete VRF Config  ===============\n')
    url = "https://" + device + "/restconf/data/Cisco-IOS-XE-native:native/router/bgp=65000/address-family/with-vrf/" \
                                "ipv4=unicast/vrf=" + name

    time.sleep(7)
    response = requests.request("DELETE", url, headers=common_data.headers, verify=False)

    common_data.printApiResponse(response)

    # Delete VRF itself
    url = "https://" + device + "/restconf/data/Cisco-IOS-XE-native:native/vrf/definition=" + name

    time.sleep(7)
    response = requests.request("DELETE", url, headers=common_data.headers, verify=False)

    common_data.printApiResponse(response)
