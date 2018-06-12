#import libary_1 as lib
import numpy as np
import importlib
import sys
sys.path.insert(0, 'C:/Users/mkris/Documents/Master/3. Semester/Robotik/code')
#imp.load_module('libary_1', 'C:/Users/mkris/Documents/Master/3. Semester/Robotik/code')
import libary_1 as robo
import robolibXXX as roboXXX
importlib.reload(robo)


#dh_para = np.array([(1.570796327, 0, 0.1519, 0), (0, -0.24365, 0, -1.570796327), (0, -0.21325, 0, 0), (1.570796327, 0, 0.11235, -1.570796327), (-1.570796327, 0, 0.08535, 0), (0, 0, 0.0819, 0)])
#alle Spalten ohne q
dh_para = np.array([(1.570796327, 0, 0.1519), (0, -0.24365, 0), (0, -0.21325, 0), (1.570796327, 0, 0.11235), (-1.570796327, 0, 0.08535), (0, 0, 0.0819)])
#home:
q = np.array([0, -1.570796327, 0, -1.570796327, 0, 0])

#q = np.array([(np.pi/4),(-np.pi/4),(np.pi/4),(np.pi/4),(np.pi/4),(np.pi/4)])
#print(dh_para)


#T=robo.dh(1.41372, 0, 0.1519, 0)
#home:
tcp = np.array([0, -0.19425, 0.69415, 0, 2.2214, -2.2214])

for i in range(7):
    winkel = robo.ik_ur(dh_para, tcp, i)
    
    q1 = winkel[0]
    q2 = winkel[1]
    q3 = winkel[2]
    q4 = winkel[3]
    q5 = winkel[4]
    q6 = winkel[5]
    
    print("Solution: ", i)
    print("q1 = ", q1, " = ", np.degrees(q1))
    print("q2 = ", q2, " = ", np.degrees(q2))
    print("q3 = ", q3, " = ", np.degrees(q3))
    print("q4 = ", q4, " = ", np.degrees(q4))
    print("q5 = ", q5, " = ", np.degrees(q5))
    print("q6 = ", q6, " = ", np.degrees(q6))
    
    i = i+1
    

#tcp = np.array([(-302,-186,557,0.4,1.3,-1.7)])
#tcp = np.array([(-563.9,-122.84,261.14,0.5907,-0.3976,-1.4705)])
#tcp = np.array([(-357.83, -194.25, 553.83, 0.7689, 1.7248, -1.7248)])
#T_0_6 = robo.rotvec_2_T(tcp)

#print("T06: " , T_0_6)

#rpy = robo.T_2_rpy(T_0_6)
#print(rpy)
#T = robo.fk_ur(dh_para,q)



#rotvec = robo.T_2_rotvec(T)
#print("rotvec = ",rotvec)
##rxryrz = robo.T_2_rpy(T)
##print(rxryrz)


#robo.rotvec_2_T(tcp)
#test = np.array([10,-20,30,40,50,60])
#robo.rotvec_2_T(test)

#record configuration um outputs zu konfigurieren
#mit spyder csv datei ausplotten