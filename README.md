# YANG Praktikum

Abgabe der Scripts für das Modul Cloud Infrastructure von Jerome Gygax und Luca Gubler.

## Getting started

Bevor ein Script ausgeführt werden kann, muss die Datei "devices_list.txt" im Unterordner data mit den gewünschten Geräten ausgefüllt werden. Jeweils ein Gerät pro Zeile, wenn möglich mit FQDN damit sicher auf das Gerät verbunden werden kann. Die Scripts lesen jedes Gerät in dieser Datei aus und führen ihre Aktionen für alle Geräte aus.

## Use Case 1 - List all services configured on the leaf switch

### Script ausführen

So kann das Script ausgeführt werden:
```
python list_vrf.py
```
Der Output kann dann wie folgt aussehen:
```
jerome@Jerome-NB:/mnt/CldInf/Praktikum14_Yang/yang/python$ python list_vrf.py
Reading configuration for sw03-pod-9.lab.ins.hsr.ch
API call status: OK!


================  Print VRF Config  ================

#  VRF                  RD              Route-Target
----------------------------------------------------------
1  Green                10.3.3.3:20     I: 200:1 E: 200:1
2  Mgmt-vrf
3  Yellow               10.3.3.3:10     I: 100:1 E: 100:1


Reading configuration for sw04-pod-9.lab.ins.hsr.ch
API call status: OK!


================  Print VRF Config  ================

#  VRF                  RD              Route-Target
----------------------------------------------------------
1  Green                10.4.4.4:20     I: 200:1 E: 200:1
2  Mgmt-vrf
3  Yellow               10.4.4.4:10     I: 100:1 E: 100:1
```
## Use Case 2 - Deploy a new service on a leaf switch

### Script ausführen
So kann das Script ausgeführt werden:
```
python deploy_service.py -r <rd> -a <asn-ip> -d <description>
```
Beispiel:
```
python deploy_service.py -r 10.9.9.9:123 -a 456:1 -d "my awesome vrf"
```

#### Arguments
* -r: route distinguisher
* -a: route-target to import/export the routes from the vrf
* -d: description of the vrf

## Use Case 3 - Remove a service from a leaf switch

### Script ausführen
So kann das Script ausgeführt werden:
```
python delete_service.py -n <name>
```

#### Arguments
* -n: name of the service to remove


## Use Case 4 - Deploy a BGP neighborship between a leaf and spine switch

### Script ausführen
So kann das Script ausgeführt werden:
```
deploy_bgp_neighbor.py -i <router_id> -l <loopback_interface-#> -r <remote_as>
```

#### Arguments
* -i: router-id of the bgp neighbor
* -l: # of the loopback interface
* -r: remote as

## Fehlermeldungen
Die Scripts geben bei einem Fehler einen Exit-Code zurück. Hier eine Auflistung um den Fehler zu identifizieren:
* 3 Nicht ausreichende Zahl an Argumenten
* 5 Falsche Argumente verwendet
* 7 Fehler beim Lesen oder Schreiben von Daten übers REST API

## Authors

* **Jerome Gygax** - *Initial work* - [gyjch](https://github.com/gyjch)
* **Luca Gubler** - *Helped Jerome* - [lucagubler](https://github.com/lucagubler)