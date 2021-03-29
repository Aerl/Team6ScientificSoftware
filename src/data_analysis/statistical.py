import numpy as np
import pandas as pd
variance_threshold = 1.0e-5


def filter_by_variance_pd(df, threshold=variance_threshold):
    """Filters entries in df by their variance. Entries with variance lower than
    threshold are dropped.

    Args:
        df (data frame): A list with the indices of the reference vectors.
        threshold (float): Threshold value used for filtering.

    Returns:
        data frame: only contains entries with high variance."""
    variance = np.var(df.values, axis=0)
    return df.drop(columns=df.columns[(variance < threshold)])


def euclidean_distance_pd(list_ref, list_comp, df):
    """Calculates the Euclidean distance (L2 norm) between pairs of entries in df.

    Args:
        list_ref (integer list): A list with the indices of the reference vectors.
        list_comp (integer list): A list with the indices of the vectors to\
        compare to.
        df (data frame): The data object.

    Returns:
        data frame: The Euclidean distance (L2 norm) for comparison vs. reference\
        vectors."""
    distances = np.zeros(len(list_ref))
    row_indices = []
    for i in range(len(list_ref)):
        distances[i] = np.linalg.norm(df.values[list_comp[i]] - df.values[list_ref[i]])
        row_indices.append(str(list_ref[i]) + ' to ' + str(list_comp[i]))
    return pd.DataFrame(data=distances, index=row_indices, columns=["EucDist"])
