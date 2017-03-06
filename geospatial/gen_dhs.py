import os
import pandas as pd
import geopandas as gp


def list_dir(target):
    return [c for c in os.listdir(target) if not c.startswith(".") and c != "output"]

DHS_GEODIR = "~/geospatial-dhs"
target_dir = os.path.expanduser(DHS_GEODIR)
countries = list_dir(target_dir)


def process_year(target_dir):
    shp_file = [f for f in list_dir(target_dir) if f.endswith(".shp")][0]
    target_file = os.path.join(target_dir, shp_file)
    cols = ["REGCODE", "ISO", "REGNAME", "REGVAR", "SVYYEAR", "geometry"]
    df =  gp.read_file(target_file)
    df = df[cols].copy()

    if not df[df.REGVAR != 'hv024'].empty:
        raise Exception("Non-province entity!")
    df["REGCODE"] = df["REGCODE"].astype(int)
    df["SVYYEAR"] = df["SVYYEAR"].astype(int)
    df["REGNAME"] = df["REGNAME"].str.title()

    return df

cf = pd.DataFrame()

for country in countries:
    country_dir = os.path.join(target_dir, country)
    years = list_dir(country_dir)
    print country, years

    for year in years:
        print year
        year_dir = os.path.join(country_dir, year)
        cf = pd.concat([process_year(year_dir), cf])
    print cf.head()

output_path = os.path.join(target_dir, "output", "dhs.shp")
cf.to_file(output_path)
