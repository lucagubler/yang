#!/usr/bin/env python

# File is part of task UC2

import requests
import json
import time
import sys
import getopt
import common_data

# Read arguments
name = ''
rd = ''
asn_ip = ''
description = ''

try:
    opts, args = getopt.getopt(sys.argv[1:], "hn:r:a:d:", [
                               "name=", "rd=", "asn_ip=", "description="])
except getopt.GetoptError:
    print('usage: deploy_service.py -n <vrf-name> -r <rd> -a <asn-ip> -d <description>')
    sys.exit(5)
for opt, arg in opts:
    if opt == '-h':
        print('usage: deploy_service.py -n <vrf-name> -r <rd> -a <asn-ip> -d <description>')
        sys.exit()
    elif opt in ("-n", "--name"):
        name = arg
    elif opt in ("-r", "--rd"):
        rd = arg
    elif opt in ("-a", "--asn_ip"):
        asn_ip = arg
    elif opt in ("-d", "--description"):
        description = arg

if name == '' or rd == '' or asn_ip == '' or description == '':
    print('Missing arguments. Use option -h for help.')
    sys.exit(3)

# Begin configuration for each device read in devices_list
with open('data/devices_list.txt') as f:
    devices = f.read().splitlines()

for device in devices:
    print('Starting configuration for ' + device)
    # First deploy VRF
    print('\n===============  Deploy VRF Config  ===============\n')

    url = "https://" + device + "/restconf/data/Cisco-IOS-XE-native:native/vrf"

    with open('data/uc2_vrf_conf.json') as jsonfile:
        payload = json.load(jsonfile)

    payload['Cisco-IOS-XE-native:vrf']['definition'][0]['name'] = name
    payload['Cisco-IOS-XE-native:vrf']['definition'][0]['rd'] = rd
    payload['Cisco-IOS-XE-native:vrf']['definition'][0]['description'] = description
    payload['Cisco-IOS-XE-native:vrf']['definition'][0]['route-target']['export'][0]['asn-ip'] = asn_ip
    payload['Cisco-IOS-XE-native:vrf']['definition'][0]['route-target']['import'][0]['asn-ip'] = asn_ip

    time.sleep(7)
    response = requests.request(
        "PATCH", url, json=payload, headers=common_data.headers, verify=False)

    common_data.printApiResponse(response)

    # Secondly deploy BGP configuration for VRF
    print('\n===============  Deploy BGP Config  ===============\n')

    url = "https://" + device + \
        "/restconf/data/Cisco-IOS-XE-native:native/router/bgp=65000/address-family/with-vrf/ipv4=unicast"

    with open('data/uc2_bgp_conf.json') as jsonfile:
        payload = json.load(jsonfile)
    payload['Cisco-IOS-XE-bgp:ipv4']['vrf'][0]['name'] = name

    time.sleep(7)
    response = requests.request(
        "PATCH", url, json=payload, headers=common_data.headers, verify=False)

    common_data.printApiResponse(response)
