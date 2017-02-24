SELECT p.poverty_geo as_poverty_geo,
   ('050AF'::text || lpad(s.adm0_code::integer::text, 5, '0'::text)) || lpad(s.adm1_code::integer::text, 5, '0'::text) AS geo,
   st_area(p.geom) AS st_area,
   st_area(st_intersection(p.geom, s.geom)) / st_area(p.geom) AS pct_overlap
  FROM spatial.poverty_l1_geo p
    JOIN spatial.cell5m_geo s ON st_intersects(p.geom, s.geom)
 WHERE (st_area(st_intersection(p.geom, s.geom)) / st_area(p.geom)) > 0.05::double precision
UNION
SELECT '040PG'::text || g.iso3 AS poverty_geo,
   g.id AS geo,
   NULL::double precision AS st_area,
   NULL::double precision AS pct_overlap
  FROM attrs.geo g
 WHERE g.level = 'adm0'::text AND (g.iso3 IN ( SELECT DISTINCT poverty_geo.iso3
          FROM attrs.poverty_geo));
