from pathlib import Path
from typing import Dict

import numpy as np
import pandas as pd


def read_files(folder)->Dict[str, pd.DataFrame]:
    """Read in all data files. The time will be the index if present.

    Parameters
    ----------
    folder : str or pathlike
        The folder where the data files are located

    Returns
    -------
    Dict[str, pd.DataFrame]
        The different data files as DataFrames in a dict
    """

    folder = Path(folder)

    filenames = ('efield.t', 'expec.t', 'npop.t', 'nstate_i.t', 'table.dat')

    nstate = np.loadtxt(folder / filenames[3], skiprows=1)
    # convert to complex
    nstate_complex = nstate[:,1::2].astype('complex') + nstate[:,2::2]*1j
    nstate_df = pd.DataFrame(nstate_complex)
    nstate_df.set_index(nstate[:,0])
    nstate_df.index.name = 'time'

    result_dict = {
        'efield' : pd.read_csv(folder / filenames[0], delim_whitespace=True).set_index('time'),
        'expec' : pd.read_csv(folder / filenames[1], delim_whitespace=True).set_index('time'),
        'npop' : pd.read_csv(folder / filenames[2], delim_whitespace=True).set_index('time'),
        'nstate_i' : nstate_df,
        'table' : pd.read_csv(folder / filenames[4], delim_whitespace=True)
    }
    return result_dict

def export_df(df:pd.DataFrame, filename):
    """Export a dataframe to a file

    Parameters
    ----------
    df : pd.DataFrame
        The frame to export
    filename : str
        The file to export to
    """
    df.to_csv(filename)