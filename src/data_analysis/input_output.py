from pathlib import Path
from typing import Dict

import numpy as np
import pandas as pd


def read_files(folder)->Dict[str, pd.DataFrame]:
    """Read in all data files.

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
    # add time again
    nstate_complex_time = np.concatenate([nstate[:,0:1], nstate_complex], axis=1)

    result_dict = {
        'efield' : pd.read_csv(folder / filenames[0], delim_whitespace=True),
        'expec' : pd.read_csv(folder / filenames[1], delim_whitespace=True),
        'npop' : pd.read_csv(folder / filenames[2], delim_whitespace=True),
        'nstate_i' : pd.DataFrame(nstate_complex_time, columns=['time'] + list(np.arange(nstate_complex.shape[1], dtype=int))),
        'table' : pd.read_csv(folder / filenames[4], delim_whitespace=True)
    }
    return result_dict