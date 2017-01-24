shp2pgsql dissolved_l1_v2.shp spatial.pov_svy_geo > pov_survey_geo.sql
shp2pgsql cell5m.shp spatial.cell5m_geo > cell5m_geo.sql
shp2pgsql dhsMap_2016.10.12.shp spatial.dhs_geo > dhs_geo.sql

# # Fix ring self-intersections
# UPDATE spatial.cell5m_geo
# SET geom = ST_MakeValid(geom)
# WHERE NOT ST_IsValid(geom)
#
#
# # create dissolved table
# CREATE TABLE poverty_l1_map AS
# (SELECT iso3, svyl1cd, ST_UNION(geom)
# FROM spatial.poverty_map
# GROUP BY iso3, svyl1cd)
