import jacobimatrix as j
import numpy as np
import importlib
import sys
sys.path.insert(0, './code')
importlib.reload(j)


dh_para = np.array([(1.570796327, 0, 0.1519), (0, -0.24365, 0), (0, -0.21325, 0), (1.570796327, 0, 0.11235), (-1.570796327, 0, 0.08535), (0, 0, 0.0819)])

#home
q = np.array([0, -1.570796327, 0, -1.570796327, 0, 0])

J = j.jacobi_ur(dh_para, q)
print(J)


v_tcp(qT, vT, dh_para)