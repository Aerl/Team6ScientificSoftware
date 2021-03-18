import numpy as np
variance_threshold = 1.0e-5


def filter_by_variance(df, threshold=variance_threshold):
    variance = np.var(df.values, axis=0)
    return df.drop(columns=df.columns[(variance < threshold)])