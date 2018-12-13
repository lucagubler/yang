#!/usr/bin/env python

# File is part of task UC4

import json
import requests
import time
import common_data
import sys
import getopt

name = ''
rd = ''
asn_ip = ''
description = ''

try:
    opts, args = getopt.getopt(sys.argv[1:], "hn:r:a:d:", ["name=", "rd=", "asn_ip=", "description="])
except getopt.GetoptError:
    print 'usage: deploy_service.py -n <vrf-name> -r <rd> -a <asn-ip> -d <description>'
    sys.exit(2)
for opt, arg in opts:
    if opt == '-h':
        print 'usage: deploy_service.py -n <vrf-name> -r <rd> -a <asn-ip> -d <description>'
        sys.exit()
    elif opt in ("-n", "--name"):
        name = arg
    elif opt in ("-r", "--rd"):
        rd = arg
    elif opt in ("-a", "--asn_ip"):
        asn_ip = arg
    elif opt in ("-d", "--description"):
        description = arg

if name == '' or rd == '' or asn_ip == '':
    print 'Please use the correct arguments. Use option -h for help.'
    sys.exit

print name
print rd
print asn_ip
print description

# with open('data/devices_list.txt') as f:
#     devices = f.read().splitlines()
#
# for device in devices:
#     print('Starting configuration for ' + device)
#     # Add BGP Neighbor
#     print('\n===============  Deploy BGP Neighbor  ==============\n')
#
#     url = "https://" + device + "/restconf/data/Cisco-IOS-XE-native:native/router/bgp=65000/neighbor"
#
#     with open('data/uc4_bgp_neighborship.json') as jsonfile:
#         payload = json.load(jsonfile)
#     payload['Cisco-IOS-XE-bgp:neighbor'][0]['id'] = r_id
#     payload['Cisco-IOS-XE-bgp:neighbor'][0]['remote-as'] = r_as
#     payload['Cisco-IOS-XE-bgp:neighbor'][0]['update-source']['Loopback'] = lo_int
#     print(payload)