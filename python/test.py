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

url = "https://sw03-pod-5.lab.ins.hsr.ch/restconf/data/Cisco-IOS-XE-native:native/router/bgp=65000/address-family/with-vrf/ipv4=unicast"

with open('uc2_bgp_conf.json') as jsonfile:
    payload = json.load(jsonfile)

print(payload)
response = requests.request(
    "PATCH", url, json=payload, headers=headers, verify=False)

print(response.status_code)