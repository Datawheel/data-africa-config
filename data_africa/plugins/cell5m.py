import pandas as pd

def crop_format(df, **kwargs):
    index = kwargs.get("index")
    df = pd.melt(df, id_vars=index, var_name="crop", value_name="harvested_area")
    is_rain_fed = df.crop.str.endswith("_r_h")
    is_irr = df.crop.str.endswith("_i_h")
    df.loc[is_rain_fed, 'water_supply'] = 'rainfed'
    df.loc[is_irr, 'water_supply'] = 'irrigated'
    df.loc[(~is_irr & ~is_rain_fed), 'water_supply'] = 'overall'
    df.crop = df.crop.str.replace("(_r_h|_i_h|_h)", "")
    return df
