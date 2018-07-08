import sys
import importlib
sys.path.insert(0, './')
import trajektorienplanung as tp
importlib.reload(tp)
import matplotlib.pyplot as plt
import numpy as np

"""
Save plots to
"""
save_to ='./plots'
name = 'movej_0-90q1'
"""
6 Achsen Trajektorieplanung
"""

vmax = 0.8
amax = 1
# Abtastrate
delta_t = 1/125


# movej q1
q1Start = 0/180*np.pi
q2Start = -90/180*np.pi
q3Start = 90/180*np.pi
q4Start = -90/180*np.pi
q5Start = -90/180*np.pi
q6Start = 0/180*np.pi

q1Target = 90/180*np.pi
q2Target = -90/180*np.pi
q3Target = 90/180*np.pi
q4Target = -90/180*np.pi
q5Target = -90/180*np.pi
q6Target = 0/180*np.pi

"""
move j with t = 10s
"""
#tges = 10
#[amax, vmax] = tp.movej_with_t_getav(q1Start, q1Target, tges)



# 3 Achsen Sync

#q1Start = 0/180*np.pi
#q2Start = -90/180*np.pi
#q3Start = 90/180*np.pi
#q4Start = -90/180*np.pi
#q5Start = -90/180*np.pi
#q6Start = 0/180*np.pi
#
#q1Target = 90/180*np.pi
#q2Target = -60/180*np.pi
#q3Target = 30/180*np.pi
#q4Target = -90/180*np.pi
#q5Target = -90/180*np.pi
#q6Target = 0/180*np.pi

a_array = np.zeros(6)
v_array = np.zeros(6)

qStart = np.array([q1Start, q2Start, q3Start, q4Start, q5Start, q6Start])
qTarget = np.array([q1Target, q2Target, q3Target, q4Target, q5Target, q6Target])

achse = tp.traj_6_axis(qStart, qTarget, vmax, amax)




tges_max = 0
for i in range(6):
    if  achse[i, 2] > tges_max:
        tges_max = achse[i, 2]
        
        
for i in range(6):
    if achse[i, 2] == 0: 
        achse[i, 2] = tges_max
        
    ts1 = achse[i, 0]
    ts2 = achse[i, 1]
    tges = achse[i, 2]
    a = achse[i, 3]
    v = achse[i, 4]
    [qt, vt, at, t] = tp.traj_sample(qStart[i], qTarget[i], ts1, ts2, tges, a, v, delta_t)
    print(qt)
    
    plt.figure(0)
   
    if (i == 0):
        plt.plot(t, qt, color = 'r', label = 'q1')
    elif (i == 1):
        plt.plot(t, qt, color = 'g', label = 'q2')
    elif (i == 2):
        plt.plot(t, qt, color = 'b', label = 'q3')
    elif (i == 3):
        plt.plot(t, qt, color = 'c', label = 'q4')
    elif (i == 4):
        plt.plot(t, qt, color = 'violet', label = 'q5')
    elif ( i == 5):
        plt.plot(t, qt, color = 'orange', label = 'q6')
    plt.xlabel('t [s]')
    plt.ylabel('q [rad]')
    plt.title( name + '_calculation')
    plt.grid(True)
    leg = plt.legend(loc='best',  shadow=True, fancybox=True)
    if i == 5:
        plt.savefig(save_to + name + '_q_calculation.png')
    
    
    
    plt.figure(1)
    plt.title( name + '_calculation')
    plt.xlabel('t [s]')
    plt.ylabel('qd [rad/s]')
    if (i == 0):
        plt.plot(t, vt, color = 'r', label = 'qd1')
    elif (i == 1):
        plt.plot(t, vt, color = 'g', label = 'qd2')
    elif (i == 2):
        plt.plot(t, vt, color = 'b', label = 'qd3')
    elif (i == 3):
        plt.plot(t, vt, color = 'c', label = 'qd4')
    elif (i == 4):
        plt.plot(t, vt, color = 'violet', label = 'qd5')
    elif ( i == 5):
        plt.plot(t, vt, color = 'orange', label = 'qd6')    
        
    plt.grid(True)
    leg = plt.legend(loc='best',  shadow=True, fancybox=True)
    if i == 5:
        plt.savefig(save_to + name + '_qd_calculation..png')
    
    
    
    plt.figure(2)
    if (i == 0):
        plt.plot(t, at, color = 'r', label = 'qdd1')
    elif (i == 1):
        plt.plot(t, at, color = 'g', label = 'qdd2')
    elif (i == 2):
        plt.plot(t, at, color = 'b', label = 'qdd3')
    elif (i == 3):
        plt.plot(t, at, color = 'c', label = 'qdd4')
    elif (i == 4):
        plt.plot(t, at, color = 'violet', label = 'qdd5')
    elif ( i == 5):
        plt.plot(t, at, color = 'orange', label = 'qdd6')     
    
    plt.xlabel('t [s]')
    plt.ylabel('qdd [rad/s^2]')
    plt.title( name + '_calculation')
    plt.grid(True)
    leg = plt.legend(loc='best',  shadow=True, fancybox=True)

    if i == 5:
        plt.savefig(save_to + name + '_qdd_calculation.png')

print("...plots saved")
plt.show() 
    
