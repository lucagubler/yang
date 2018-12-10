#!/usr/bin/env python

# File is part of task UC2

import json
import requests
import time
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
    # First deploy VRF
    print('\n\n===============  Deploy VRF Config  ===============\n\n')
    time.sleep(7)

    url = "https://" + device + "/restconf/data/Cisco-IOS-XE-native:native/vrf"

    with open('uc2_vrf_conf.json') as jsonfile:
        payload = json.load(jsonfile)
    response = requests.request("PATCH", url, json=payload, headers=headers, verify=False)

    print('Response OK if there is no output below this line: \n' + response.text)


    # Secondly deploy BGP configuration for VRF
    print('\n\n===============  Deploy BGP Config  ===============\n\n')
    time.sleep(7)

    url = "https://" + device + "/restconf/data/Cisco-IOS-XE-native:native/router/bgp=65000"

    with open('uc2_bgp_conf.json') as jsonfile:
        payload = json.load(jsonfile)

    # Sometimes getting following error message:
    # missing element: name in /ios:native/ios:router/ios-bgp:bgp[ios-bgp:id='65000']/ios-bgp:address-family/ios-bgp:with-vrf/ios-bgp:ipv4[ios-bgp:af-name='unicast']/ios-bgp:vrf
    # same PATCH works just fine in Postman.
    response = requests.request("PATCH", url, json=payload, headers=headers, verify=False)

    print('Response OK if there is no output below this line: \n' + response.text)