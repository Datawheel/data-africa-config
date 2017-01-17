import pandas as pd

def crop_format(df, **kwargs):
    index = kwargs.get("index")
    mode = kwargs.get("mode", "h")
    vname = "harvested_area" if mode == "h" else "value_of_production"
    df = pd.melt(df, id_vars=index, var_name="crop", value_name=vname)
    is_rain_fed = df.crop.str.endswith("_r_{}".format(mode))
    is_irr = df.crop.str.endswith("_i_{}".format(mode))
    df.loc[is_rain_fed, 'water_supply'] = 'rainfed'
    df.loc[is_irr, 'water_supply'] = 'irrigated'
    df.loc[(~is_irr & ~is_rain_fed), 'water_supply'] = 'overall'
    df.crop = df.crop.str.replace("(_r_{0}|_i_{0}|_{0})".format(mode), "")
    return df
