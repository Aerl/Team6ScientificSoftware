import numpy as np
import pandas as pd


def autocorr(df:pd.DataFrame)->pd.DataFrame:
    df_new = df.copy()
    for c in df_new:
        df_new[c] = df_new[c].autocorr()

    return df_new
