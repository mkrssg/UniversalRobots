#!/usr/bin/env python

import matplotlib.pyplot as plt

import sys
sys.path.append('..')
import rtde.csv_reader as csv_reader

openstr = 'movel_distance-y=400_simulation.csv'
saveplots = './simulation/'
with open('C:/Users/mkris/Documents/Master/3. Semester/Robotik/code/plots_simulation/csv/'+ openstr) as csvfile:
    r = csv_reader.CSVReader(csvfile)

# plot

# q
fig = plt.figure()
plt.plot(r.timestamp, r.target_q_0, color='r', label='q1')
plt.plot(r.timestamp, r.target_q_1, color='g', label='q2')
plt.plot(r.timestamp, r.target_q_2, color='b', label='q3')
plt.plot(r.timestamp, r.target_q_3, color='c',label='q4')
plt.plot(r.timestamp, r.target_q_4, color='violet', label='q5')
plt.plot(r.timestamp, r.target_q_5, color='orange', label='q6')

plt.title(openstr[:-4])
plt.xlabel('t [s]')
plt.ylabel('q [rad]')
plt.grid(True)
leg = plt.legend(loc='lower left',  shadow=True, fancybox=True)
#plt.savefig(saveplots + openstr[:-4] + '_q.png')



#qd
plt.figure()
plt.plot(r.timestamp, r.target_qd_0, color='r', label='qd1')
plt.plot(r.timestamp, r.target_qd_1, color='g', label='qd2')
plt.plot(r.timestamp, r.target_qd_2, color='b', label='qd3')
plt.plot(r.timestamp, r.target_qd_3, color='c',label='qd4')
plt.plot(r.timestamp, r.target_qd_4, color='violet', label='qd5')
plt.plot(r.timestamp, r.target_qd_5, color='orange', label='qd6')

plt.title(openstr[:-4])
plt.xlabel('t [s]')
plt.ylabel('qd [rad/s]')
plt.grid(True)
leg = plt.legend(loc='best',  shadow=True, fancybox=True)
#plt.savefig(saveplots + openstr[:-4] + '_qd.png')




#qdd
plt.figure()
plt.plot(r.timestamp, r.target_qdd_0, color='r', label='qdd1')
plt.plot(r.timestamp, r.target_qdd_1, color='g', label='qdd2')
plt.plot(r.timestamp, r.target_qdd_2, color='b', label='qdd3')
plt.plot(r.timestamp, r.target_qdd_3, color='c',label='qdd4')
plt.plot(r.timestamp, r.target_qdd_4, color='violet', label='qdd5')
plt.plot(r.timestamp, r.target_qdd_5, color='orange', label='qdd6')

plt.title(openstr[:-4])
plt.xlabel('t [s]')
plt.ylabel('qdd [rad/s^2]')
plt.grid(True)
leg = plt.legend(loc='best',  shadow=True, fancybox=True)
#plt.savefig(saveplots + openstr[:-4] + '_qdd.png')



#move l - tcp pose
plt.figure()
plt.plot(r.timestamp, r.actual_TCP_pose_0, color='r', label='x')
plt.plot(r.timestamp, r.actual_TCP_pose_1, color='g', label='y')
plt.plot(r.timestamp, r.actual_TCP_pose_2, color='b', label='z')

plt.title(openstr[:-4])
plt.xlabel('t [s]')
plt.ylabel('position [m]')
plt.grid(True)
leg = plt.legend(loc='best',  shadow=True, fancybox=True)
plt.savefig(saveplots + openstr[:-4] + '_TCP_position.png')
#plt.show()

#move l - tcp geschwindigkeit
plt.figure()
plt.plot(r.timestamp, r.actual_TCP_speed_0, color='r', label='x')
plt.plot(r.timestamp, r.actual_TCP_speed_1, color='g', label='y')
plt.plot(r.timestamp, r.actual_TCP_speed_2, color='b', label='z')

plt.title(openstr[:-4])
plt.xlabel('t [s]')
plt.ylabel('v [rad/s]')
plt.grid(True)
leg = plt.legend(loc='best',  shadow=True, fancybox=True)
plt.savefig(saveplots + openstr[:-4] + '_TCP_speed.png')
#plt.show()


