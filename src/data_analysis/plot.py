import matplotlib.pyplot as plt


def plot_df(df, filename):
    """Plot a dataframe

    Parameters
    ----------
    df : pd.DataFrame
        The df to plot
    filename : str
        The file to save as.
    """
    df.plot()
    plt.show()
    plt.savefig(filename)
    return
