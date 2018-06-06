# -*- coding: utf-8 -*-

import socket
import numpy as np
from time import sleep

HOST = "192.168.25.130"
PORT = 30002

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

#1 Achse
#q1 = 0/180*np.pi
#q2 = -60/180*np.pi
#q3 = 30/180*np.pi
#q4 = -90/180*np.pi
#q5 = -90/180*np.pi
#q6 = 0/180*np.pi

#sleep(5)
#
#q1 = 90/180*np.pi
#q2 = -90/180*np.pi
#q3 = 90/180*np.pi
#q4 = -90/180*np.pi
#q5 = -90/180*np.pi
#q6 = 0/180*np.pi
##
#3 Achsen
# von:
#q1 = 0/180*np.pi
#q2 = -90/180*np.pi
#q3 = 90/180*np.pi
#q4 = -90/180*np.pi
#q5 = -90/180*np.pi
#q6 = 0/180*np.pi
# zu:
#q1 = 90/180*np.pi
#q2 = 0/180*np.pi
#q3 = -90/180*np.pi
#q4 = -90/180*np.pi
#q5 = -90/180*np.pi
#q6 = 0/180*np.pi

#bei allen 3 Achsen gleichzeitig bewgegen zu:
#q1 = 90/180*np.pi
#q2 = -30/180*np.pi
#q3 = 60/180*np.pi
#q4 = -90/180*np.pi
#q5 = -90/180*np.pi
#q6 = 0/180*np.pi

#Beschleinigung
#a = 1.0
#v = 0.8
#t = 10

#command = "movej([" + str(q1) + "," + str(q2) + ","+str(q3)+","+str(q4)+","+str(q5)+","+str(q6)+"], a=" + str(a) +", v=" +str(v)+")\n"
#command = "movej([" + str(q1) + "," + str(q2) + ","+str(q3)+","+str(q4)+","+str(q5)+","+str(q6)+"],t=" + str(t) +")\n"

#command = "movej([" + str(q1) + "," + str(q2) + ","+str(q3)+","+str(q4)+","+str(q5)+","+str(q6)+"], a=" + str(a) +", v=" +str(v)+")\n"

"""
#6. movel x 400 with a,v/ time t --> movel_x400
a = 1.0
v = 0.2
pHome = np.array([-0.300,-0.200,0.300,2.2214,2.2214,0])
pTarget = np.array([-0.300,0.200,0.300,2.2214,2.2214,0])


command = "movej(p[" + str(pHome[0]) + "," + str(pHome[1]) + "," + str(pHome[2]) +"," + str(pHome[3]) +"," + str(pHome[4]) +"," + str(pHome[5]) +"], a=" + str(a) + ", v=" + str(v)  + ")\n"
#command = "movel(p[" + str(pTarget[0]) + "," + str(pTarget[1]) + "," + str(pTarget[2]) +"," + str(pTarget[3]) +"," + str(pTarget[4]) +"," + str(pTarget[5]) +"], a=" + str(a) + ", v=" + str(v) + ")\n"




#command = "movel(p[" + str(pTarget[0]) + "," + str(pTarget[1]) + "," + str(pTarget[2]) +"," + str(pTarget[3]) +"," + str(pTarget[4]) +"," + str(pTarget[5]) +"], t= " + str(t) + ")\n"
s.send(command.encode('ascii'))
"""


#7. movel x 400 with a,v/ time t: movel_x400_Singular
a = 1.0
v = 0.15
# pHome = np.array([0.200,-0.200,0.400,2.4186,-2.4185,2.4185])
# pTarget = np.array([0.200,0.200,0.400,2.4186,-2.4185,2.4185])
#michi:
pHome = np.array([-0.150,-0.200,0.300,2.2214,2.2214,0])
pTarget = np.array([-0.150,0.200,0.300,2.2214,2.2214,0])


#command = "movej(p[" + str(pHome[0]) + "," + str(pHome[1]) + "," + str(pHome[2]) +"," + str(pHome[3]) +"," + str(pHome[4]) +"," + str(pHome[5]) +"], a=" + str(a) + ", v=" + str(v)  + ")\n"
command = "movel(p[" + str(pTarget[0]) + "," + str(pTarget[1]) + "," + str(pTarget[2]) +"," + str(pTarget[3]) +"," + str(pTarget[4]) +"," + str(pTarget[5]) +"], a=" + str(a) + ", v=" + str(v) + ")\n"
#command = "movel(p[" + str(pTarget[0]) + "," + str(pTarget[1]) + "," + str(pTarget[2]) +"," + str(pTarget[3]) +"," + str(pTarget[4]) +"," + str(pTarget[5]) +"], t= " + str(t) + ")\n"
s.send(command.encode('ascii'))
