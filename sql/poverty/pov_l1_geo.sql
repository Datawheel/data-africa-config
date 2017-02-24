SELECT "right"(poverty_map.svycode::text, 4) AS year,
   poverty_map.iso3,
   poverty_map.svyl1cd,
   st_union(poverty_map.geom) AS geom,
       CASE
           WHEN poverty_map.iso3::text = ANY (ARRAY['NGA'::character varying, 'TZA'::character varying, 'SEN'::character varying, 'UGA'::character varying]::text[]) THEN (('050PG'::text || poverty_map.iso3::text) || lpad(poverty_map.svyl1cd::integer::text, 5, '0'::text)) || "right"(poverty_map.svycode::text, 4)
           ELSE ('050PG'::text || poverty_map.iso3::text) || lpad(poverty_map.svyl1cd::integer::text, 5, '0'::text)
       END AS poverty_geo
  FROM spatial.poverty_map
 GROUP BY ("right"(poverty_map.svycode::text, 4)), poverty_map.iso3, poverty_map.svyl1cd;
