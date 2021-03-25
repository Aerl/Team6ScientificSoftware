import pytest
import pandas as pd

import numpy as np

from data_analysis import numerical

class build_wf:
    def __init__(self, dim1, dim2, myval):
        self.dim1 = dim1
        self.dim2 = dim2
        self.myval = myval

    def init_array(self):
        arr = np.ones((self.dim1, self.dim2), dtype=complex)
        return arr*self.myval

    def init_vector(self):
        arr = np.ones((self.dim1,), dtype=complex)
        return arr*self.myval

@pytest.fixture
def test_wf():
    obj = build_wf(3, 3, 1.0)
    return obj.init_array()

@pytest.fixture
def ref_auto():
    obj = build_wf(3, 3, 3.0)
    return obj.init_vector()

def test_autocorr_single():
    test_array = np.random.rand(8)
    # norm the test data
    test_array = test_array / np.sqrt(np.sum(np.square(test_array)))
    pytest.approx(numerical.autocorr_single_tp(test_array, 0), 1)
    
def test_autocorr(test_wf, ref_auto):
    print(numerical.autocorr(pd.DataFrame(test_wf)).values)
    assert np.allclose(numerical.autocorr(pd.DataFrame(test_wf)).values, ref_auto)