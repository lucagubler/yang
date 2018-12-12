#!/usr/bin/env python

# File is part of task UC4

import requests, json, time, sys
import common_data
import getopt

# Read arguments
r_id = ''
lo_int = ''
r_as = ''

try:
    opts, args = getopt.getopt(sys.argv[1:], "hi:l:r:", ["r_id=", "lo_int=", "r_as="])
except getopt.GetoptError:
    print 'usage: deploy_bgp_neighbor.py -i <r_id> -l <lo_int> -r <r_as>'
    sys.exit(2)
for opt, arg in opts:
    if opt == '-h':
        print 'usage: deploy_bgp_neighbor.py -i <r_id> -l <lo_int> -r <r_as>'
        sys.exit()
    elif opt in ("-i", "--r_id"):
        r_id = arg
    elif opt in ("-l", "--lo_int"):
        lo_int = arg
    elif opt in ("-r", "--r_as"):
        r_as = arg

if r_id == '' or lo_int == '' or r_as == '':
    print 'Please use the correct arguments. Use option -h for help.'
    sys.exit

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

    payload['Cisco-IOS-XE-bgp:neighbor'][0]['id'] = r_id

    time.sleep(7)
    response = requests.request("PATCH", url, json=payload, headers=common_data.headers, verify=False)

    common_data.printApiResponse(response)

    url = "https://" + device + "/restconf/data/Cisco-IOS-XE-native:native/router/bgp=65000/address-family/no-vrf/" \
                                "vpnv6=unicast/vpnv6-unicast/neighbor"
    time.sleep(7)
    response = requests.request("PATCH", url, json=payload, headers=common_data.headers, verify=False)

    common_data.printApiResponse(response)