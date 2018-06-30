import sys
import importlib
sys.path.insert(0, 'C:/Users/mkris/Documents/Master/3. Semester/Robotik/code')

import trajektorienplanung as tp
import jacobimatrix as jc
import libary_1 as rl
importlib.reload(tp)
importlib.reload(jc)
import matplotlib.pyplot as plt
import numpy as np

"""
Save plots to
"""
save_to ='C:/Users/mkris/Documents/Master/3. Semester/Robotik/code/trajektorien_plots/'
name = 'movel_distance-y=400_singularity'

# non singularity
#pStart = np.array([-0.250,-0.200, 0.300,2.2214,2.2214,0])
#pTarget = np.array([-0.250, 0.200, 0.300,2.2214,2.2214,0])
#pStart = np.array([-250,-200, 300,2.2214,2.2214,0])
#pTarget = np.array([-250, 200, 300,2.2214,2.2214,0])
# singularity
#pStart = np.array([-0.150,-0.200, 0.300,2.2214,2.2214,0])
#pTarget = np.array([-0.150, 0.200, 0.300,2.2214,2.2214,0])
# 
#T = rl.rotvec_2_T(pStart)
#pNeu = rl.T_2_rotvec(T)
#
#
#print(pNeu)


""" neue Werte Fixing"""
"""non singu"""
#pStart = np.array([0.300,-0.200,0.350,2,-2,2])
#pTarget = np.array([0.300,0.200,0.350,2,-2,2])

"""singularity"""
pStart = np.array([0.200,-0.200,0.350,2,-2,2])
pTarget = np.array([0.200,0.200,0.350,2,-2,2])

# florens
#pStart = np.array([300,-200,400,2.4186,-2.4185,2.4185])
#pTarget = np.array([300,200,400,2.4186,-2.4185,2.4185])
    #mm

# Felix
#pStart = np.array([0.250,-0.300, 0.380,0.6453,1.4727,0.6453])
#pTarget = np.array([0.250, 0.100, 0.380,0.6453,1.4727,0.6453])


#dh_para = np.array([(1.570796327, 0, 151.9), (0, -243.65, 0), (0, -213.25, 0), (1.570796327, 0, 112.35), (-1.570796327, 0, 85.35), (0, 0, 81.9)])
dh_para = np.array([(1.570796327, 0, 0.1519), (0, -0.24365, 0), (0, -0.21325, 0), (1.570796327, 0, 0.11235), (-1.570796327, 0, 0.08535), (0, 0, 0.0819)])

amax = 1.0
vmax = 0.2
delta_t = 1/125
sol = 1

#for sol in range(8):
#    print("Solution: ", sol)
#    [pose_t, pose_vt, pose_at, v_tcp, a_tcp, t] = tp.traj_poseSample (pStart, pTarget, vmax, amax, delta_t)
#    """ get q """
#    q_t = tp.ik_pose(pose_t, dh_para, sol)
#    v_t = jc.vt(q_t, pose_vt, dh_para)
#    v_tcp = jc.v_tcp(q_t, pose_vt, dh_para)

print("Solution: ", sol)
[pose_t, pose_vt, pose_at, v_tcp, a_tcp, t] = tp.traj_poseSample (pStart, pTarget, vmax, amax, delta_t)
""" get q """
q_t = tp.ik_pose(pose_t, dh_para, sol)
v_t = jc.vt(q_t, pose_vt, dh_para)
#v_tcp = jc.v_tcp(q_t, pose_vt, dh_para)
print(v_tcp)

#print("Solution: ", sol)
#[pose_t, pose_vt, pose_at, v_tcp, a_tcp, t] = tp.traj_poseSample (pStart, pTarget, vmax, amax, delta_t)
#""" get q """
#q_t = tp.ik_pose(pose_t, dh_para, sol)
#v_t = jc.vt(q_t, pose_vt, dh_para)
#v_tcp = jc.v_tcp(q_t, pose_vt, dh_para)
    
    #print(np.rad2deg(q_t[0,:]))
    

"""
[xyzrxryrzT, xyzrxryrzVT, xyzrxryrzAT, vTcpT, aTcpT, t] = tp.traj_samplePose(pStart, pTarget, vmax, amax, delta_t)
#tp.plotTrajPose(xyzrxryrzT, xyzrxryrzVT, xyzrxryrzAT, vTcpT, aTcpT, t)

q_t = tp.traj_sampleAxesIk(xyzrxryrzT, dh_para, sol)
vT = jc.vt(qT, xyzrxryrzVT, dh_para)

pose_t = xyzrxryrzT
"""

#plt.plot(t, pose_t[:,0], color='r', label='x')
#plt.plot(t, pose_t[:,1], color='g', label='y')
#plt.plot(t, pose_t[:,2], color='b', label='z')
#plt.title('Position')
#plt.xlabel('t in s')
#plt.ylabel('position')
#leg = plt.legend(loc='best',  shadow=True, fancybox=True)
#plt.show()

for i in range(6):
    plt.figure(1)
    #    plt.plot(t, q_t)
    if (i == 0):
        plt.plot(t, q_t[:,i], color = 'r', label = 'q1')
    elif (i == 1):
        plt.plot(t, q_t[:,i], color = 'g', label = 'q2')
    elif (i == 2):
        plt.plot(t, q_t[:,i], color = 'b', label = 'q3')
    elif (i == 3):
        plt.plot(t, q_t[:,i], color = 'c', label = 'q4')
    elif (i == 4):
        plt.plot(t, q_t[:,i], color = 'violet', label = 'q5')
    elif ( i == 5):
        plt.plot(t, q_t[:,i], color = 'orange', label = 'q6')
    plt.title(name + '_q_calculation')
    plt.xlabel('t [s]')
    plt.ylabel('q [rad]')
    plt.grid(True)
    leg = plt.legend(loc='best',  shadow=True, fancybox=True)
plt.savefig(save_to + name + '_q_calculation.png')
plt.show()
#print("qt:   ", np.rad2deg(q_t[0,:]))

for i in range(6):
    plt.figure(2)
    #    plt.plot(t, q_t)
    if (i == 0):
        plt.plot(t, v_t[:,i], color = 'r', label = 'q1')
    elif (i == 1):
        plt.plot(t, v_t[:,i], color = 'g', label = 'q2')
    elif (i == 2):
        plt.plot(t, v_t[:,i], color = 'b', label = 'q3')
    elif (i == 3):
        plt.plot(t, v_t[:,i], color = 'c', label = 'q4')
    elif (i == 4):
        plt.plot(t, v_t[:,i], color = 'violet', label = 'q5')
    elif ( i == 5):
        plt.plot(t, v_t[:,i], color = 'orange', label = 'q6')
    plt.title(name + '_qd_calculation')
    plt.xlabel('t [s]')
    plt.ylabel('qd [rad/s]')
    plt.grid(True)
    leg = plt.legend(loc='best',  shadow=True, fancybox=True)
plt.savefig(save_to + name + '_qd_calculation.png')
plt.show()

#
#plt.plot(t, pose_vt )
#plt.title('Velocity')
#plt.xlabel('t in s')
#plt.ylabel('v')
#leg = plt.legend(loc='best',  shadow=True, fancybox=True)
#plt.show()
#
#
#
#plt.plot(t, pose_at)
#plt.title('Acceleration')
#plt.xlabel('t in s')
#plt.ylabel('a')
#leg = plt.legend(loc='best',  shadow=True, fancybox=True)
#plt.show() 
#
#plt.plot(pose_t[:,0], pose_t[:,1] )
#plt.title('xy')
#plt.xlabel('x')
#plt.ylabel('y')
#leg = plt.legend(loc='best',  shadow=True, fancybox=True)
#plt.show()
#
#
#plt.plot(t, v_t )
#plt.title('Velocity')
#plt.xlabel('t in s')
#plt.ylabel('v')
#leg = plt.legend(loc='best',  shadow=True, fancybox=True)
#plt.show()