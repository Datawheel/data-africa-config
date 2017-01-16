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

    df = df.pivot_table(index=idx + ["poverty_level"],
                        columns=["val_kind"],
                        values="value")
    return df.reset_index()
