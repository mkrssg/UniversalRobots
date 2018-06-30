import numpy as np
import importlib
import sys
sys.path.insert(0, 'C:/Users/mkris/Documents/Master/3. Semester/Robotik/code')
import libary_1 as robo
importlib.reload(robo)

def jacobi_ur(dh_para, q):
    J = np.zeros((q.size, q.size))
    T = np.eye(4)
    T_0_i = np.eye(4)
    
    T_0_6 = robo.fk_ur(dh_para, q)
    p = T_0_6[0:3, 3]
    
    i = 0
    for i in range(6):
        
        z_i = T_0_i[0:3, 2]
        p_i = T_0_i[0:3, 3]
        
        T = robo.dh(dh_para[i,0], dh_para[i,1], dh_para[i,2], q[i]) 
        T_0_i = np.dot(T_0_i, T)
        
        r = p - p_i
        
        J[0:3, i] = np.cross(z_i, r)
        J[3:6, i] = z_i
        
    return J

"""
tcp Geschwindigkeit über t = J_q_t * q_t
""" 

def v_tcp(q_t, v_t, dh_para):
    v_tcp = np.zeros((q_t.shape[0],6))
    
    for t in range(q_t.shape[0]):
        J_t = jacobi_ur(dh_para, q_t[t])
        v_tcp[t] = np.dot(J_t, v_t[t])
    return v_tcp

"""
Gelenkwinkelgeschwindigkeit --> movej
"""
def vt(q_t, pose_vt, dh_para):
    v_t = np.zeros(q_t.shape)
    
    for t in range(q_t.shape[0]):
        J_t = jacobi_ur(dh_para, q_t[t])
        try: 
            J_t_inv = np.linalg.inv(J_t)
            v_t[t] = np.dot(J_t_inv, pose_vt[t])
        except:
            v_t[t] = np.zeros(6)
    
    return v_t
