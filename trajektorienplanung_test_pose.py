import sys
import importlib
sys.path.insert(0, 'C:/Users/mkris/Documents/Master/3. Semester/Robotik/code')
import trajektorienplanung as tp
importlib.reload(tp)
import matplotlib.pyplot as plt
import numpy as np

pStart = np.array([-298.6, -112.35, 313.65, 2.2214, 2.2214, 0])
pTarget = np.array([112.35, -298.6, 313.65, 0, 3.142, 0])
amax = 1.0
vmax = 0.8
delta_t = 1/125
[pose_t, pose_vt, pose_at, t] = tp.traj_poseSample (pStart, pTarget, vmax, amax, delta_t)
print("[pose_t, pose_vt, pose_at, t]","\n", [pose_t, pose_vt, pose_at, t])

plt.plot(t, pose_t)
plt.title('Position')
plt.show()
plt.plot(t, pose_vt )
plt.title('Velocity')
plt.show()
plt.plot(t, pose_at)
plt.title('Acceleration')
plt.show() 