# YANG Praktikum

Abgabe der Scripts für das Modul Cloud Infrastructure von Gerome Gygax und Luca Gubler.

## Getting started

Nachfolgend wird gezeigt, wie die Scripts funktionieren und aufgerufen werden können

## Use Case 1 - List all services configured on the leaf switch

### Script ausführen

So kann das Script ausgeführt werden:
```
python list_vrf.py
```

## Use Case 2 - Deploy a new service on a leaf switch

### Script ausführen
So kann das Script ausgeführt werden:
```
python deploy_service.py -r <rd> -a <asn-ip> -d <description>
```

#### Arguments
* -r: route distinguisher
* -a: <!-- TODO -->
* -d: <!-- TODO -->

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
python deploy_bgp_neighbor.py -i <r_id> -l <lo_int> -r <r_as>
```

#### Arguments
* -i: <!-- TODO -->
* -l: <!-- TODO -->
* -r: <!-- TODO -->

## Authors

* **Jerome Gygax** - *Initial work* - [gyjch](https://github.com/gyjch)
* **Luca Gubler** - *Helped Jerome* - [lucagubler](https://github.com/lucagubler)