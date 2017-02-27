import pandas as pd

def tidy(df, **kwargs):
    idx = kwargs.get("index")
    df = pd.melt(df, id_vars=idx, var_name="variable")
    # set poverty levels
    df.loc[df.variable.str.endswith('_ppp1'), 'poverty_level'] = 'ppp1'
    df.loc[df.variable.str.endswith('_ppp2'), 'poverty_level'] = 'ppp2'
    # set val kinds
    df.loc[df.variable.str.startswith('povgap_'), 'val_kind'] = 'povgap'
    df.loc[df.variable.str.startswith('hc_'), 'val_kind'] = 'hc'
    df.loc[df.variable.str.startswith('sevpov_'), 'val_kind'] = 'sevpov'
    df.loc[df.variable.str.startswith('num_'), 'val_kind'] = 'num'

    df = df.pivot_table(index=idx + ["poverty_level"],
                        columns=["val_kind"],
                        values="value")
    return df.reset_index()

def manually_fix_geo_ids(df, **kwargs):
    pov_id = 'poverty_geo' if not 'id' in kwargs else kwargs['id']
    rules = [
        {"year": 2003, "iso3": "NGA", "region": False},
        {"year": 2012, "iso3": "NGA", "region": True},

        {"year": 2000, "iso3": "TZA", "region": False},
        {"year": 2007, "iso3": "TZA", "region": False},
        {"year": 2012, "iso3": "TZA", "region": True},

        {"year": 2001, "iso3": "SEN", "region": False},
        {"year": 2005, "iso3": "SEN", "region": False},
        {"year": 2011, "iso3": "SEN", "region": False},

        {"year": 2002, "iso3": "UGA", "region": True},
        {"year": 2005, "iso3": "UGA", "region": True},
        {"year": 2009, "iso3": "UGA", "region": True},
        {"year": 2012, "iso3": "UGA", "region": True},
        {"year": 2013, "iso3": "UGA", "region": True},

        {"year": 1998, "iso3": "BDI", "region": None},
        {"year": 2006, "iso3": "BDI", "region": None}

    ]

    for rule in rules:
        year, iso3, region = rule["year"], rule["iso3"], rule["region"]
        df.loc[(df.year == year) & (df.iso3 == iso3), pov_id] = df[pov_id] + df.year.astype(str)

    return df
