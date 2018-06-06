#!/usr/bin/env

import matplotlib.pyplot as plt

import sys
sys.path.append('C:/Users/mkris/Documents/Master/3. Semester/Robotik/code/rtde_client_3.5')
import rtde.csv_reader as csv_reader

#
#"""
#sources
#"""
#simfolder = '../simulation/'
#robofolder = '../roboter/'
#movej_30 = 'movej_0-30q1'
#movej_90 = 'movej_0-90q1'
#movej_3Achsen = 'movej_3_Achsen_zu_90,-60,30,-90,-90,0'
#t = "_t=10s"
#simu = "_simu"
#csv = ".csv"
#
#"""
#move j 0-30 q1 simu
#"""
#with open(simfolder+movej_30+simu+csv) as csvfile:
#    r = csv_reader.CSVReader(csvfile)
#
## plot
#
#fig = plt.figure()
#plt.plot(r.timestamp, r.target_q_0)
#plt.plot(r.timestamp, r.target_q_1)
#plt.plot(r.timestamp, r.target_q_2)
#plt.plot(r.timestamp, r.target_q_3)
#plt.plot(r.timestamp, r.target_q_4)
#plt.plot(r.timestamp, r.target_q_5)
#
#plt.savefig(openstr[:-4] + '_q.png')
##ax = fig.add_axes([0,0,1,1])
#
#plt.figure()
#plt.plot(r.timestamp, r.target_qd_0)
#plt.plot(r.timestamp, r.target_qd_1)
#plt.plot(r.timestamp, r.target_qd_2)
#plt.plot(r.timestamp, r.target_qd_3)
#plt.plot(r.timestamp, r.target_qd_4)
#plt.plot(r.timestamp, r.target_qd_5)
#
#plt.savefig(openstr[:-4] + '_qd.png')
#
#



folder = 'C:/Users/mkris/Documents/Master/3. Semester/Robotik/code/rtde_client_3.5/examples/simulation/'
csv = 'movej_0-90q1_simu.csv'
with open(folder + csv) as csvfile:
    r = csv_reader.CSVReader(csvfile)

#plt einstellungen

#plt.grid(True)
#plt.ylabel('Gelenkwinkel in Rad')
#plt.xlabel('Zeit in s')
#plt.legend()


# plot
#q
fig = plt.figure()
plt.plot(r.timestamp, r.target_q_0, color='r', label='q0')
plt.plot(r.timestamp, r.target_q_1, color='g', label='q1')
plt.plot(r.timestamp, r.target_q_2, color='b', label='q2')
plt.plot(r.timestamp, r.target_q_3, color='c',label='q3')
plt.plot(r.timestamp, r.target_q_4)
plt.plot(r.timestamp, r.target_q_5)

plt.savefig(csv[:-4] + '_q.png')

#v
#fig = plt.figure()
#plt.plot(r.timestamp, r.target_qd_0, color='r', label='qd0')
#plt.plot(r.timestamp, r.target_qd_1, color='g', label='qd1')
#plt.plot(r.timestamp, r.target_qd_2, color='b', label='qd2')
#plt.plot(r.timestamp, r.target_qd_3, color='c', label='qd3')
#plt.plot(r.timestamp, r.target_qd_4, color='magenta', label='qd4')
#plt.plot(r.timestamp, r.target_qd_5, color='ornage', label='qd5')
#
#
#plt.savefig(csv[:-4] + '_qd.png')
#
##a
#fig = plt.figure()
#plt.plot(r.timestamp, r.target_qdd_0, 'r', label='qdd0')
#plt.plot(r.timestamp, r.target_qdd_1, 'g', label='qdd1')
#plt.plot(r.timestamp, r.target_qdd_2, 'b', label='qdd2')
#plt.plot(r.timestamp, r.target_qdd_3, 'c', label='qdd3')
#plt.plot(r.timestamp, r.target_qdd_4, 'magenta', label='qdd4')
#plt.plot(r.timestamp, r.target_qdd_5, 'ornage', label='qdd5')
#
#
#plt.savefig(csv[:-4] + '_qd.png')




plt.show()

