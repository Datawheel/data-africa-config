CREATE TABLE spatial.poverty_l1_map AS
    (SELECT iso3, svyl1cd, ST_UNION(geom)
     FROM spatial.poverty_map
     GROUP BY iso3, svyl1cd)
