shp2json dhs.shp | geo2topo -q 1e5 | toposimplify -p .005 > dhs_adm1.json
