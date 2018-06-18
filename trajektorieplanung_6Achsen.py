import sys
import importlib
sys.path.insert(0, 'C:/Users/mkris/Documents/Master/3. Semester/Robotik/code')
import trajektorienplanung as tp
importlib.reload(tp)
import matplotlib.pyplot as plt
import numpy as np

"""
Save plots to
"""
save_to ='C:/Users/mkris/Documents/Master/3. Semester/Robotik/code/trajektorien_plots'

"""
6 Achsen Trajektorieplanung
"""

vmax = 1
amax = 2
# Abtastrate
delta_t = 1/125

q1Start = 0
q2Start = 0
q3Start = 0
q4Start = 0
q5Start = 0
q6Start = 0

q1Target = 1
q2Target = 0
q3Target = 3
q4Target = 0
q5Target = 0
q6Target = 0

a_array = np.zeros(6)
v_array = np.zeros(6)

qStart = np.array([q1Start, q2Start, q3Start, q4Start, q5Start, q6Start])
qTarget = np.array([q1Target, q2Target, q3Target, q4Target, q5Target, q6Target])

ts1 = np.zeros(6)
ts2 = np.zeros(6)
tges = np.zeros(6)

# Matrix zeile für jede Achse mit: ts1, ts2, tges, a, v
achse = np.zeros((6,5))

tges_max = 0
i_lead_axis = 0



"""
ts1 ts2 tges
"""
for i in range(6):
    [ts1[i],ts2[i],tges[i]] = tp.traj_timestamps(qStart[i], qTarget[i], amax, vmax)
    print("Achse",i+1," : ", "ts1= ", ts1[i],"ts2= ", ts2[i],"tges= ", tges[i])
    
    achse[i, 0:3] = [ts1[i],ts2[i],tges[i]]
    if  achse[i, 2] > tges_max:
        tges_max = achse[i, 2]
        i_lead_axis = i
        
    #[a, v] = tp.traj_getav(qStart[i], qTarget[i], ts1[i], tges[i])
    #i += 1
    
print("Führungsachse = Achse",i_lead_axis+1)


for i in range(6):
    # neues a und v für alle Achsen außer Führungsachse
    [achse[i,3], achse[i,4]] = tp.traj_getav(qStart[i], qTarget[i], ts1[i_lead_axis], tges[i_lead_axis])
    # ts1 ts2 tges der Führungsachse entsprechen jetzt den anderen bewegenden Achsen
    if achse[i, 2] != 0: #dann bewegt sich achse
        achse[i, 0] = achse[i_lead_axis, 0]
        achse[i, 1] = achse[i_lead_axis, 1]
        achse[i, 2] = achse[i_lead_axis, 2]  
    
print("Achsen ts1, ts2, tges, a, v : ", "\n", achse)


for i in range(6):
    if achse[i, 2] == 0: 
        achse[i, 2] = tges_max
        
    ts1 = achse[i, 0]
    ts2 = achse[i, 1]
    tges = achse[i, 2]
    a = achse[i, 3]
    v = achse[i, 4]
    [qt, vt, at, t] = tp.traj_sample(qStart[i], qTarget[i], ts1, ts2, tges, a, v, delta_t)
    
    plt.figure(0)
    plt.plot(t, qt)
    plt.xlabel('t in s')
    plt.ylabel('q')
    plt.title('Position')
    if i == 5:
        plt.savefig(save_to + '/position.png')
    
    plt.figure(1)
    plt.title('Velocity')
    plt.xlabel('t in s')
    plt.ylabel('v')
    plt.plot(t,vt)
    if i == 5:
        plt.savefig(save_to + '/velocity.png')
    
    plt.figure(2)
    plt.plot(t,at)
    plt.xlabel('t in s')
    plt.ylabel('a')
    plt.title('Acceleration')
    if i == 5:
        plt.savefig(save_to + '/acceleration.png')

print("...plots saved")
plt.show() 

