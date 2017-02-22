SELECT ('050HG'::text || p.iso::text) || lpad(p.regcd::integer::text, 3, '0'::text) || p.svyyr AS 	dhs_geo,
('050AF'::text || lpad(s.adm0_code::integer::text, 5, '0'::text)) || lpad(s.adm1_code::integer::text, 5, '0'::text) AS geo,
st_area(p.geom) AS st_area,
st_area(st_intersection(p.geom, s.geom)) / st_area(p.geom) AS pct_overlap

FROM spatial.dhs_geo p
JOIN spatial.cell5m_geo s ON st_intersects(p.geom, s.geom)
WHERE (st_area(st_intersection(p.geom, s.geom)) / st_area(p.geom)) > 0.05::double precision
AND p.regcd IS NOT NULL
AND p.regvr::text = 'hv024'::text

UNION

SELECT '040HG'::text || geo.iso2 AS dhs_geo,
    geo.id AS geo,
    NULL::double precision AS st_area,
    NULL::double precision AS pct_overlap
   FROM attrs.geo
  WHERE geo.level = 'adm0'::text;
