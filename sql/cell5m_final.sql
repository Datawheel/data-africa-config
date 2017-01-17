-- Unified ADM0/ADM1 geometry table
SELECT '040AF'::text || lpad(cell5m_geo.adm0_code::integer::text, 5, '0'::text) AS geo,
   st_union(cell5m_geo.geom) AS geom
  FROM spatial.cell5m_geo
 GROUP BY cell5m_geo.adm0_code
UNION
SELECT ('050AF'::text || lpad(cell5m_geo.adm0_code::integer::text, 5, '0'::text)) || lpad(cell5m_geo.adm1_code::integer::text, 5, '0'::text) AS geo,
   st_union(cell5m_geo.geom) AS geom
  FROM spatial.cell5m_geo
 GROUP BY cell5m_geo.adm0_code, cell5m_geo.adm1_code;

-- CREATE INDEX geom_idx ON spatial.cell5m_final USING gist (geom)
