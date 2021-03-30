import pytest
import pandas as pd

import numpy as np

from data_analysis import autocorr, autocorr_single_tp


class build_wf:
    def __init__(self, dim1, dim2):
        self.dim1 = dim1
        self.dim2 = dim2

    def init_array(self, myval):
        arr = np.ones((self.dim1, self.dim2), dtype=complex)
        return arr * myval

    def init_vector(self, myval):
        arr = np.ones((self.dim1,), dtype=complex)
        return arr * myval


@pytest.fixture(scope='module')
def init_obj():
    obj = build_wf(3, 3)
    return obj


@pytest.fixture
def test_wf(init_obj):
    return init_obj.init_array(1)


@pytest.fixture
def ref_auto(init_obj):
    return init_obj.init_vector(3)


def test_autocorr_single():
    test_array = np.random.rand(8)
    # norm the test data
    test_array = test_array / np.sqrt(np.sum(np.square(test_array)))
    pytest.approx(autocorr_single_tp(test_array, 0), 1)


def test_autocorr(test_wf, ref_auto):
    assert np.allclose(autocorr(pd.DataFrame(test_wf)).values, ref_auto)
