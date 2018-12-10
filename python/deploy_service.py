#!/usr/bin/env python

# File is part of task UC2

import json
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

headers = {
    'Accept': "application/yang-data+json",
    'Content-Type': "application/yang-data+json",
    'Authorization': "Basic aW5zOmluc0BsYWI=",
    }

# First deploy VRF
print('\n\n===============  Deploy VRF Config  ===============\n\n')

url = "https://sw03-pod-5.lab.ins.hsr.ch/restconf/data/Cisco-IOS-XE-native:native/vrf"

with open('uc2_vrf_conf.json') as jsonfile:
    payload = json.load(jsonfile)
response = requests.request("PATCH", url, json=payload, headers=headers, verify=False)

print('Response OK if there is no output below this line: \n' + response.text)

# Secondly deploy BGP configuration for VRF
print('\n\n===============  Deploy BGP Config  ===============\n\n')

url = "https://sw03-pod-5.lab.ins.hsr.ch/restconf/data/Cisco-IOS-XE-native:native/router/bgp=65000"

with open('uc2_bgp_conf.json') as jsonfile:
    payload = json.load(jsonfile)

response = requests.request("PATCH", url, json=payload, headers=headers, verify=False)

print('Response OK if there is no output below this line: \n' + response.text)