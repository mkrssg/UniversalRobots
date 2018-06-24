# -*- coding: utf-8 -*-

"""
URSim
password: ur --> easybot
IP: 192.168.175.128

check robot TCP first: Installation --> TCP!!!

Port 
30001 --> Primary Client: URScript Commands 10Hz
30002 --> Secondary Client: URScript Commands 10Hz
30003 --> Real Time Client: URScript Commands 125Hz
30004 --> Real Time Data Exchange: Various Data 125Hz
"""

import numpy as np
import socket
from time import sleep

#1. Secondary Client Connection
#URSIM
#HOST = "192.168.175.128" # URSim IP
#HOST = "192.168.182.128" # URsim IP Prakt

#ROBOT
HOST = "192.168.25.130"

PORT = 30002 # port



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

"""
#1. movej axis1 30deg with a,v --> movej_Dreieck
a = 1.0
v = 0.8
qStart = np.array([np.deg2rad(0),np.deg2rad(-90),np.deg2rad(-90),np.deg2rad(0),np.deg2rad(90),np.deg2rad(0)])
qTarget = np.array([np.deg2rad(30),np.deg2rad(-90),np.deg2rad(-90),np.deg2rad(0),np.deg2rad(90),np.deg2rad(0)])


command = "movej([" + str(qStart[0]) + "," + str(qStart[1]) + "," + str(qStart[2]) +"," + str(qStart[3]) +"," + str(qStart[4]) +"," + str(qStart[5]) +"])\n"
s.send(command.encode('ascii'))

sleep(5)

command = "movej([" + str(qTarget[0]) + "," + str(qTarget[1]) + "," + str(qTarget[2]) +"," + str(qTarget[3]) +"," + str(qTarget[4]) +"," + str(qTarget[5]) +"], a=" + str(a) + ", v=" + str(v) + ")\n"
s.send(command.encode('ascii'))
"""

"""
#2. movej axis1 90deg with a,v --> movej_Trapez
a = 1.0
v = 0.8
qStart = np.array([np.deg2rad(0),np.deg2rad(-90),np.deg2rad(-90),np.deg2rad(0),np.deg2rad(90),np.deg2rad(0)])
qTarget = np.array([np.deg2rad(90),np.deg2rad(-90),np.deg2rad(-90),np.deg2rad(0),np.deg2rad(90),np.deg2rad(0)])


command = "movej([" + str(qStart[0]) + "," + str(qStart[1]) + "," + str(qStart[2]) +"," + str(qStart[3]) +"," + str(qStart[4]) +"," + str(qStart[5]) +"])\n"
s.send(command.encode('ascii'))

sleep(8)

command = "movej([" + str(qTarget[0]) + "," + str(qTarget[1]) + "," + str(qTarget[2]) +"," + str(qTarget[3]) +"," + str(qTarget[4]) +"," + str(qTarget[5]) +"], a=" + str(a) + ", v=" + str(v) + ")\n"
s.send(command.encode('ascii'))
"""

"""
#3. movej axis1 30deg in time t --> movej_Dreieck_Zeit
t = 3
qStart = np.array([np.deg2rad(0),np.deg2rad(-90),np.deg2rad(-90),np.deg2rad(0),np.deg2rad(90),np.deg2rad(0)])
qTarget = np.array([np.deg2rad(30),np.deg2rad(-90),np.deg2rad(-90),np.deg2rad(0),np.deg2rad(90),np.deg2rad(0)])


command = "movej([" + str(qStart[0]) + "," + str(qStart[1]) + "," + str(qStart[2]) +"," + str(qStart[3]) +"," + str(qStart[4]) +"," + str(qStart[5]) +"])\n"
s.send(command.encode('ascii'))

sleep(5)

command = "movej([" + str(qTarget[0]) + "," + str(qTarget[1]) + "," + str(qTarget[2]) +"," + str(qTarget[3]) +"," + str(qTarget[4]) +"," + str(qTarget[5]) +"],t= " + str(t) + ")\n"
s.send(command.encode('ascii'))
"""

"""
#4. movej axis1 90deg in time t --> movej_Trapez_Zeit
t = 6
qStart = np.array([np.deg2rad(0),np.deg2rad(-90),np.deg2rad(-90),np.deg2rad(0),np.deg2rad(90),np.deg2rad(0)])
qTarget = np.array([np.deg2rad(90),np.deg2rad(-90),np.deg2rad(-90),np.deg2rad(0),np.deg2rad(90),np.deg2rad(0)])


command = "movej([" + str(qStart[0]) + "," + str(qStart[1]) + "," + str(qStart[2]) +"," + str(qStart[3]) +"," + str(qStart[4]) +"," + str(qStart[5]) + "])\n"
s.send(command.encode('ascii'))

sleep(8)

command = "movej([" + str(qTarget[0]) + "," + str(qTarget[1]) + "," + str(qTarget[2]) +"," + str(qTarget[3]) +"," + str(qTarget[4]) +"," + str(qTarget[5]) +"], t= " + str(t) + ")\n"
s.send(command.encode('ascii'))
"""

"""
#5. movej Achse1 90deg, Achse2 60deg, Achse3 30deg in time t --> movej_Synchron
a = 1.0
v = 0.8
t = 6
qStart = np.array([np.deg2rad(0),np.deg2rad(-90),np.deg2rad(-90),np.deg2rad(0),np.deg2rad(90),np.deg2rad(0)])
qTarget = np.array([np.deg2rad(90),np.deg2rad(-30),np.deg2rad(-60),np.deg2rad(0),np.deg2rad(90),np.deg2rad(0)])


command = "movej([" + str(qStart[0]) + "," + str(qStart[1]) + "," + str(qStart[2]) +"," + str(qStart[3]) +"," + str(qStart[4]) +"," + str(qStart[5]) + "])\n"
s.send(command.encode('ascii'))

sleep(8)

command = "movej([" + str(qTarget[0]) + "," + str(qTarget[1]) + "," + str(qTarget[2]) +"," + str(qTarget[3]) +"," + str(qTarget[4]) +"," + str(qTarget[5]) +"], t= " + str(t) + ")\n"
s.send(command.encode('ascii'))
"""

"""
#6. movel x 400 with a,v --> movel_x400
a = 1.0
v = 0.2

#qInit = np.array([np.deg2rad(30),np.deg2rad(-90),np.deg2rad(-90),np.deg2rad(0),np.deg2rad(90),np.deg2rad(0)])
qInit = np.array([np.deg2rad(-20.21),np.deg2rad(-107.27),np.deg2rad(-91.88),np.deg2rad(19.15),np.deg2rad(110.22),np.deg2rad(0.01)])
pHome = np.array([0.300,-0.200,0.400,2.4186,-2.4185,2.4185])
pTarget = np.array([0.300,0.200,0.400,2.4186,-2.4185,2.4185])

#1. Position near Start
command = "movej([" + str(qInit[0]) + "," + str(qInit[1]) + "," + str(qInit[2]) +"," + str(qInit[3]) +"," + str(qInit[4]) +"," + str(qInit[5]) +"] )\n"
s.send(command.encode('ascii'))

sleep(5)

#2. Start Position
command = "movej(p[" + str(pHome[0]) + "," + str(pHome[1]) + "," + str(pHome[2]) +"," + str(pHome[3]) +"," + str(pHome[4]) +"," + str(pHome[5]) +"] )\n"
s.send(command.encode('ascii'))

sleep(2)

#3. movel_x400
command = "movel(p[" + str(pTarget[0]) + "," + str(pTarget[1]) + "," + str(pTarget[2]) +"," + str(pTarget[3]) +"," + str(pTarget[4]) +"," + str(pTarget[5]) +"], a=" + str(a) + ", v=" + str(v) + ")\n"
s.send(command.encode('ascii'))

#movel_x400_Zeit
#command = "movel(p[" + str(pTarget[0]) + "," + str(pTarget[1]) + "," + str(pTarget[2]) +"," + str(pTarget[3]) +"," + str(pTarget[4]) +"," + str(pTarget[5]) +"], t= " + str(t) + ")\n"
"""


#7. movel x 400 mit a,v nahe Singularität: movel_x400_Singular
a = 1.0
v = 0.2

#qInit = np.array([np.deg2rad(30),np.deg2rad(-90),np.deg2rad(-90),np.deg2rad(0),np.deg2rad(90),np.deg2rad(0)])
qInit = np.array([np.deg2rad(-30.51),np.deg2rad(-91.41),np.deg2rad(-110.87),np.deg2rad(22.28),np.deg2rad(120.52),np.deg2rad(0.01)])
#non singularity
pHome = np.array([-0.250,-0.200, 0.300,2.2214,2.2214,0])
pTarget = np.array([-0.250, 0.200, 0.300,2.2214,2.2214,0])
# singularity
#pHome = np.array([-0.150,-0.200, 0.300,2.2214,2.2214,0])
#pTarget = np.array([-0.150, 0.200, 0.300,2.2214,2.2214,0])

#1. Position near Start
# command = "movej([" + str(qInit[0]) + "," + str(qInit[1]) + "," + str(qInit[2]) +"," + str(qInit[3]) +"," + str(qInit[4]) +"," + str(qInit[5]) +"] )\n"
# s.send(command.encode('ascii'))

# sleep(5)

#2. Start Position
#command = "movej(p[" + str(pHome[0]) + "," + str(pHome[1]) + "," + str(pHome[2]) +"," + str(pHome[3]) +"," + str(pHome[4]) +"," + str(pHome[5]) +"] )\n"
#s.send(command.encode('ascii'))

#sleep(6)

#3. movel_x400_Singular
command = "movel(p[" + str(pTarget[0]) + "," + str(pTarget[1]) + "," + str(pTarget[2]) +"," + str(pTarget[3]) +"," + str(pTarget[4]) +"," + str(pTarget[5]) +"], a=" + str(a) + ", v=" + str(v) + ")\n"
s.send(command.encode('ascii'))

#movel_x400_Singular_Zeit
#command = "movel(p[" + str(pTarget[0]) + "," + str(pTarget[1]) + "," + str(pTarget[2]) +"," + str(pTarget[3]) +"," + str(pTarget[4]) +"," + str(pTarget[5]) +"], t= " + str(t) + ")\n"





#record data via record.py
"""
Use this script as an executable to record output data from the robot and save it to a csv file.
Optional arguments:
    
--host: name of host or IP address to connect to (default: localhost) --> change to ip: no extra host parameter when Function call
parser.add_argument('--host', default='192.168.175.128', help='name of host to connect to (localhost)')

--samples: specific number of samples to record (otherwise the program will record data until receiving SIGINT/Ctrl+C)
parser.add_argument('--samples', type=int, default=0, help='number of samples to record')

--config: XML configuration file to use - it will use the recipe with key 'out' (default: record_configuration.xml)
parser.add_argument('--config', default='record_configuration.xml', help='data configuration file to use (record_configuration.xml)')

--output: data output file to write to - an existing file will be overwritten (default: robot_data.csv)
parser.add_argument('--output', default='robot_data.csv', help='data output file to write to (robot_data.csv)')

"""

# example_plotting.py
"""
Provides a simple way to read and plot the data from a csv file recorded with the record.py.
"""