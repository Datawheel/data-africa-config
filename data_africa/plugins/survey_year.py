def convert(df, **kwargs):
    df.Survey = df.Survey.str.replace(" DHS", "")
    df['start_year'] = df.Survey.str.split("-").apply(lambda x: x[0])
    df.loc[df.Survey.str.contains("-"), 'year'] = df.loc[df.Survey.str.contains("-"), 'Survey'].str.split("-").apply(lambda x: x[0][:2] + x[1])
    df.loc[~df.Survey.str.contains("-"), 'year'] = df.start_year
    return df
