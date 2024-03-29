# 
import numpy as np

class C02S07E01(object):
    idx = 0
    ts = np.array([[0.5, 0.8, 0.4], [1.8, 0.3, 0.3], [-2.2, -1.3, 3.5]])

    def __init__(self):
        self.name = "apps.mml.c02.s07.c02_s07_e01.C02S07E01"

    def startup(self, args={}):
        print('基变换矩阵 v0.0.1')
        B = np.array([[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]])
        #B_tilde = self.generate_base_from_base(B)
        #print(B_tilde)
        C = np.array([[1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0]])
        A_Phi = np.array([[1.0, 2.0, 0.0], [-1.0, -1.0, 3.0], [3.0, 7.0, 1.0], [-1.0, 2.0, 4.0]])
        print('shape: {0}; \n{1};'.format(A_Phi.shape, A_Phi))
        x = A_Phi[:,0]
        print('x: shape: {0}; {1};'.format(x.shape, x))
        b1 = np.matmul(A_Phi.T, x)
        print('shape: {0}; {1};'.format(b1.shape, b1))


    def vector_linear_combination(self, base_v, low=-10.0, high=10.0):
        i_debug = 1
        if 1 == i_debug:
            t = C02S07E01.ts[C02S07E01.idx]
            C02S07E01.idx += 1
        else:
            t = np.random.uniform(low, high, (base_v.shape[1],))
        v = t[0] * base_v[0] + t[1] * base_v[1] + t[2] * base_v[2]
        return v

    def generate_base_from_base(self, base_v):
        b_0 = self.vector_linear_combination(base_v)
        b_1 = self.vector_linear_combination(base_v)
        b_2 = self.vector_linear_combination(base_v)
        return np.array([b_0, b_1, b_2]).T