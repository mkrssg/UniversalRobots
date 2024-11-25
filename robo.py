#import libary_1 as lib
import numpy as np
import importlib
import sys
sys.path.insert(0, './code')
import robolibXXX as robo



dh_para = np.array([(1.570796327, 0, 0.1519), (0, -0.24365, 0), (0, -0.21325, 0), (1.570796327, 0, 0.11235), (-1.570796327, 0, 0.08535), (0, 0, 0.0819)])
#home:
q = np.array([0, -1.570796327, 0, -1.570796327, 0, 0])


#test ausgangspose assignment
tcp = np.array([-0.2986, -0.11235, 0.31365, 2.2214, 2.2214, -2.2214])

"""
in mm
"""



for i in range(8):
    winkel = robo.ik_ur(dh_para, tcp, i)
    
    q1 = winkel[0]
    q2 = winkel[1]
    q3 = winkel[2]
    q4 = winkel[3]
    q5 = winkel[4]
    q6 = winkel[5]
    
    print("Solution: ", i+1)
    print("q1 = ", q1, " = ", np.rad2deg(q1))
    print("q2 = ", q2, " = ", np.rad2deg(q2))
    print("q3 = ", q3, " = ", np.rad2deg(q3))
    print("q4 = ", q4, " = ", np.rad2deg(q4))
    print("q5 = ", q5, " = ", np.rad2deg(q5))
    print("q6 = ", q6, " = ", np.rad2deg(q6))
    
    i = i+1
    
