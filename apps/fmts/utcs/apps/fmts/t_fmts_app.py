#
import unittest
import numpy as np
import torch as torch

class TFmtsApp(unittest.TestCase):
    def test_preprocess_X(self):
        X = np.array([[
            1.0, 1.1, 1.2, 1.3, 1.4,
            2.0, 2.1, 2.2, 2.3, 2.4,
            3.0, 3.1, 3.2, 3.3, 3.4,
            4.0, 4.1, 4.2, 4.3, 4.4,
            5.0, 5.1, 5.2, 5.3, 5.4,
            6.0, 6.1, 6.2, 6.3, 6.4,
            7.0, 7.1, 7.2, 7.3, 7.4,
            8.0, 8.1, 8.2, 8.3, 8.4,
            9.0, 9.1, 9.2, 9.3, 9.4,
            10.0, 10.1, 10.2, 10.3, 10.4,
            11.0, 11.1, 11.2, 11.3, 11.4
        ]])
        X = torch.from_numpy(X)
        print('X: {0};'.format(X.shape))
        X = X.view(1, -1, 5)
        print('shape: {0};'.format(X.shape))
        print(X)