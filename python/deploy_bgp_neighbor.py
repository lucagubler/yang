#!/usr/bin/env python

# File is part of task UC4

import requests, json, time, sys
import common_data

# Read arguments
if(len(sys.argv) < 3):
    print('Usage: deploy_bgp_neighbor.py <router-id> <loopback-interface> <remote-asn>')
    quit(2)
r_id = sys.argv[1]
lo_int = sys.argv[2]
r_as = sys.argv[3]

# Begin configuration for each device read in devices_list
with open('data/devices_list.txt') as f:
    devices = f.read().splitlines()

for device in devices:
    print('Starting configuration for ' + device)
    # Add BGP Neighbor
    print('\n===============  Deploy BGP Neighbor  ==============\n')

    url = "https://" + device + "/restconf/data/Cisco-IOS-XE-native:native/router/bgp=65000/neighbor"

    # Read template json
    with open('data/uc4_bgp_neighborship.json') as jsonfile:
        payload = json.load(jsonfile)
    # Edit values for valid configuration
    payload['Cisco-IOS-XE-bgp:neighbor'][0]['id'] = r_id
    payload['Cisco-IOS-XE-bgp:neighbor'][0]['update-source']['Loopback'] = lo_int
    payload['Cisco-IOS-XE-bgp:neighbor'][0]['remote-as'] = r_as
    time.sleep(7)
    response = requests.request("PATCH", url, json=payload, headers=common_data.headers, verify=False)

    common_data.printApiResponse(response)

    # Add new neighbor to VPNv* configuration
    print('\n===============  Add VPNv* Configuration  ==============\n')
    url = "https://" + device + "/restconf/data/Cisco-IOS-XE-native:native/router/bgp=65000/address-family/no-vrf/" \
                                "vpnv4=unicast/vpnv4-unicast/neighbor"

    with open('data/uc4_bgp_neighborship_vpn.json') as jsonfile:
        payload = json.load(jsonfile)
    time.sleep(7)
    response = requests.request("PATCH", url, json=payload, headers=common_data.headers, verify=False)

    common_data.printApiResponse(response)

    url = "https://" + device + "/restconf/data/Cisco-IOS-XE-native:native/router/bgp=65000/address-family/no-vrf/" \
                                "vpnv6=unicast/vpnv6-unicast/neighbor"
    time.sleep(7)
    response = requests.request("PATCH", url, json=payload, headers=common_data.headers, verify=False)
    
    common_data.printApiResponse(response)