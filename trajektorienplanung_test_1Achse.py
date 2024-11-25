import sys
import importlib
sys.path.insert(0, './code')
import trajektorienplanung as tp
importlib.reload(tp)
import matplotlib.pyplot as plt

vmax = 0.8
amax = 1.0
qStart = 1
qTarget = 2
delta_t = 1/125

[ts1, ts2, tges] = tp.traj_timestamps(qStart, qTarget, amax, vmax)
print(ts1,ts2,tges)

[a, v] = tp.traj_getav(qStart, qTarget, ts1, tges) 
print(a,v)

[tS1, tS2, tGes] = tp.traj_timestamps(qStart, qTarget, a, v)
print(tS1, tS2, tGes)

[qt, vt, at, t] = tp.traj_sample(qStart, qTarget, ts1, ts2, tges, amax, vmax, delta_t) 

plt.plot(t, qt)
plt.title('Position')
plt.show()
plt.plot(t, vt )
plt.title('Velocity')
plt.show()
plt.plot(t, at)
plt.title('Acceleration')
plt.show() 

print(ts1)
