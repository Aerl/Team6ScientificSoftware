import unittest

import numpy as np

from src.data_analysis import numerical

class TestNumerical(unittest.TestCase):
    def test_autocorr_single(self):
        test_array = np.random.rand(8)
        # norm the test data
        test_array = test_array / np.sqrt(np.sum(np.square(test_array)))
        self.assertAlmostEqual(numerical.autocorr_single_tp(test_array, 0), 1)