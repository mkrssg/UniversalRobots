import sys
import importlib
sys.path.insert(0, 'C:/Users/mkris/Documents/Master/3. Semester/Robotik/code')
import trajektorienplanung as tp
importlib.reload(tp)
import matplotlib.pyplot as plt
import numpy as np

# non singularity
pStart = np.array([-0.250,-0.200, 0.300,2.2214,2.2214,0])
pTarget = np.array([-0.250, 0.200, 0.300,2.2214,2.2214,0])

# singularity
#pStart = np.array([-0.150,-0.200, 0.300,2.2214,2.2214,0])
#pTarget = np.array([-0.150, 0.200, 0.300,2.2214,2.2214,0])

#dh_para = np.array([(1.570796327, 0, 151.9), (0, -243.65, 0), (0, -213.25, 0), (1.570796327, 0, 112.35), (-1.570796327, 0, 85.35), (0, 0, 81.9)])
dh_para = np.array([(1.570796327, 0, 0.1519), (0, -0.24365, 0), (0, -0.21325, 0), (1.570796327, 0, 0.11235), (-1.570796327, 0, 0.08535), (0, 0, 0.0819)])

amax = 1.0
vmax = 0.2
delta_t = 1/125

[pose_t, pose_vt, pose_at, t] = tp.traj_poseSample (pStart, pTarget, vmax, amax, delta_t)
""" get q """
q_t = tp.ik_pose(pStart, pTarget, vmax, amax, delta_t, dh_para)
print(q_t)

#print("[pose_t, pose_vt, pose_at, t]","\n", [pose_t, pose_vt, pose_at, t])

plt.plot(t, pose_t[:,0], color='r', label='x')
plt.plot(t, pose_t[:,1], color='g', label='y')
plt.plot(t, pose_t[:,2], color='b', label='z')
plt.title('Position')
plt.xlabel('t in s')
plt.ylabel('position')
leg = plt.legend(loc='best',  shadow=True, fancybox=True)
plt.show()

plt.plot(t, q_t)
plt.title('q')
plt.xlabel('t in s')
plt.ylabel('q')
leg = plt.legend(loc='best',  shadow=True, fancybox=True)
plt.show()


plt.plot(t, pose_vt )
plt.title('Velocity')
plt.xlabel('t in s')
plt.ylabel('v')
leg = plt.legend(loc='best',  shadow=True, fancybox=True)
plt.show()

plt.plot(t, pose_at)
plt.title('Acceleration')
plt.xlabel('t in s')
plt.ylabel('a')
leg = plt.legend(loc='best',  shadow=True, fancybox=True)
plt.show() 

plt.plot(pose_t[:,0], pose_t[:,1] )
plt.title('xy')
plt.xlabel('x')
plt.ylabel('y')
leg = plt.legend(loc='best',  shadow=True, fancybox=True)
plt.show()