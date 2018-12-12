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

### Use Case 2 - Deploy a new service on a leaf switch

#### Deploy Service
So kann das Script ausgeführt werden:
```
python deploy_service.py -r <rd> -a <asn-ip> -d <description>
```

#### Deploy BGP neighbor
So kann das Script ausgeführt werden:
```
python deploy_service.py -r <rd> -a <asn-ip> -d <description>
```