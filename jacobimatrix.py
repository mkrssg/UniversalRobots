import numpy as np
import importlib
import sys
sys.path.insert(0, 'C:/Users/mkris/Documents/Master/3. Semester/Robotik/code')
import libary_1 as robo
importlib.reload(robo)

def jacobi_ur(dh_para, q):
    J = np.zeros([q.size, q.size])
    T = np.eye(4)
    T_0_i = np.eye(4)
    
    T_0_6 = robo.fk_ur(dh_para, q)
    p = T_0_6[0:3, 3]
    
    i = 0
    for i in range(6):
        T = robo.dh(dh_para[i,0], dh_para[i,1], dh_para[i,2], dh_para[i,3] + q[i])  ####
        T_0_i = np.dot(T_0_i, T)
        z_i = T_0_i[0:3, 2]
        p_i = T_0_i[0:3, 3]
        r = p - p_i
        J[0:3, i] = np.cross(z_i, r)
        J[3:6, i] = z_i
        
    return J