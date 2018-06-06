import numpy as np

def rotx(a):
    ca = np.cos(a)
    sa = np.sin(a)
    T = np.array([(1, 0, 0, 0), (0, ca, -sa, 0,), (0, sa, ca, 0), (0, 0, 0, 1)])
    return T

def roty(a):
    ca = np.cos(a)
    sa = np.sin(a)
    T = np.array([(ca, 0, sa, 0),(0, 1, 0, 0,), (-sa, 0, ca, 0), (0, 0, 0, 1)])
    return T

def rotz(a):
    #Rotation about z
    ca = np.cos(a)
    sa = np.sin(a)
    T = np.array([(ca, -sa, 0, 0),(sa, ca, 0, 0,), (0, 0, 1, 0), (0, 0, 0, 1)])
    return T

def transl(x, y, z):
    #Translation about x y z
    T = np.array([(1, 0, 0, x),(0, 1, 0, y,), (0, 0, 1, z), (0, 0, 0, 1)])
    #print("Translation: ", T)
    return T

def Tinv(T):
    #Inverse of homogeneous trafo matrix
    R = T[0:3, 0:3]
    Ri = R.transpose()          #R inverse
    Ti = np.eye(4)
    Ti[0:3, : ][:, 0:3] = Ri 	#weist Ri den Zellen zu
    Ti[0:3, : ][:, 3:4] = -(Ri.dot(T[0:3, 3:4]))
    return Ti

def T_2_rpy(T):
    # T to roll(x, gamma) pitch(y, beta) yaw(z, alpha)
    
    b = np.arctan2(-T[2][0], np.sqrt(np.exp(T[0][0])+np.exp(T[1][0])))
    cb = np.cos(b)
    a = np.arctan2(T[1][0]/cb, T[0][0]/cb)
    g = np.arctan2(T[2][1]/cb, T[2][2]/cb) #gamma
    return np.array([g, b, a])

def rpy_2_T(xyzrpy):
	#roll pitch yaw to matrix S.13
    #x, y, z, g, b, a = xyzrpy   # richtig?!
#    g, b, a = xyzrpy
#
#    ca = np.cos(a)
#    cb = np.cos(b)
#    cg = np.cos(g)
#    sa = np.sin(a)
#    sb = np.sin(b)
#    sg = np.sin(g)
#    
#    R = np.array[(ca*cb, ca*sb*sg-sa*cg, ca*sb*cg+sa*sg),(sa*cb, sa*sb*sg+ca*cg, sa*sb*cg - ca*sg),(-sb, cb*sg, cb*cg)]
#    #T = rotvec_2_T(R)
    #T = np.array[(ca*cb, ca*sb*sg-sa*cg, ca*sb*cg+sa*sg, 0),(sa*cb, sa*sb*sg+ca*cg, sa*sb*cg - ca*sg, 0),(-sb, cb*sg, cb*cg, 0), (0, 0, 0, 1)]
    
    #T = np.dot(rotx(xyzrpy[3]), roty(xyzrpy[4]), rotz(xyzrpy[5]))
    T = np.dot(rotx(xyzrpy[5]), roty(xyzrpy[4]), rotz(xyzrpy[3])) # S.17

    return T

def T_2_rotvec(T):
	#Matrix to rotation vector representation
    x = T[0][3]
    y = T[1][3]
    z = T[2][3]
    
    #Rotation
    R = np.eye(3)
    R[0:3,0:3] = T[0:3, 0:3]

    theta = np.arccos(((R[0, 0] + R[1, 1] + R[2, 2]) - 1) / 2)
    
    if np.abs(np.sin(theta)) < 1e-6:
        rx = 0
        ry = 0
        rz = 0
        
    else:
        multi = 1 / (2 * np.sin(theta))
        
        rx = multi * (R[2, 1] - R[1, 2]) * theta
        ry = multi * (R[0, 2] - R[2, 0]) * theta
        rz = multi * (R[1, 0] - R[0, 1]) * theta
    
#    theta = np.arccos((T[0][0]+T[1][1]+T[2][2]-1)/2)
#    K_A_ = (1/2*np.sin(theta))*np.array([(T[2][1]-T[1][2]),(T[0][2]-T[2][0]),(T[1][0]-T[0][1])])
#    K_A = K_A_ * theta
#    print(K_A)
    
#    rx = np.arccos(T[1][1])
#    ry = np.arcsin(T[0][2])
#    rz = np.arcsin(-1*T[0][1])
#    print("rx, ry, rz : ", rx, ry, rz)
    
    return np.array([x,y,z,rx,ry,rz])

    # kinematik grundlagen 2
	#rotation vector representation to matrix #S.19?
#    R = rpy_2_T(xyzrxryrz)
#    #print("R2 = ", R)
#    t = transl((xyzrxryrz[0]), (xyzrxryrz[1]), (xyzrxryrz[2]))
#    T = np.dot(t, R)        #eignetlich R, t
#    print("T = ", T)
    #T = np.array([(xyzrxryrz[0][0], xyzrxryrz[0][1], xyzrxryrz[0][2], 0), (xyzrxryrz[0][3], xyzrxryrz[0][4], xyzrxryrz[0][5], 0), (0, 0, 1, 0), (0, 0, 0, 1)]) 
    #T = np.array([(-302,-186,557, 0),(0.4,1.3,-1.7,0), (0,0,1,0), (0,0,0,1)])
    #funktioniert es so oder jedes Element einzeln in T einfügen?
    #T = np.array[(ca*cb, ca*sb*sg-sa*cg, ca*sb*cg+sa*sg, 0),(sa*cb, sa*sb*sg+ca*cg, sa*sb*cg - ca*sg, 0),(-sb, cb*sg, cb*cg, 0), (0, 0, 0, 1)]
def rotvec_2_T(xyzrxryrz):
    """
    rotation vector representation to matrix
    """
    x = xyzrxryrz[0]
    y = xyzrxryrz[1]
    z = xyzrxryrz[2]
    rx = xyzrxryrz[3]
    ry = xyzrxryrz[4]
    rz = xyzrxryrz[5]
    
    T = np.eye(4)
    
    #Translation
    T[0,3] = x
    T[1,3] = y
    T[2,3] = z 
    
    R = np.eye(4)
    R = np.dot(rotx(rx), np.dot(roty(ry), rotz(rz)))
    #R = np.dot(np.dot(rotz(rz), roty(ry)), rotx(rx))
    
    T[0:3,0:3] = R[0:3, 0:3]
   
    
    return T

def dh(alpha, a, d, theta):
#Denavit-Hartenberg (classic)
    ct = np.cos(theta)
    st = np.sin(theta)
    ca = np.cos(alpha)
    sa = np.sin(alpha)
		
    T = np.array([(ct, -st*ca, st*sa, a*ct),(st, ct*ca, -ct*sa, a*st),(0, sa, ca, d),(0, 0, 0, 1)])
    return T

def dhm(alpha, a, d, theta):
#Denavit-Hartenberg (modified)
    ct = np.cos(theta)
    st = np.sin(theta)
    ca = np.cos(alpha)
    sa = np.sin(alpha)
    
    T = np.array([(ct, -st, 0, a), (st*ca, ct*ca, -sa, -d*sa), (st*sa, ct*sa, ca, d*ca), (0, 0, 0, 1)])
    return T


def fk_ur(dh_para, q):
#dh_para alle SPalten außer die mit q
#forward Kinematics for UR type robots
    #Vorwärtskinematik
# ca 5 Funktionen incl Hilfsfunktionen
       
#    T_0_1 = rotz(q[0])
#    # rotx (90grad)
#    R_1_2 = np.dot(rotx(1.57079), rotz(q[1]))
#    l1x = dh_para[0][2]
#    l1z = 0 #????
#    T_1_2 = np.dot(R_1_2, transl(l1x, 0, l1z))
#    T_2_3 = np.dot(rotz(q[2]), transl(dh_para[1][1],0,0))
#    T_3_4 = np.dot(rotz(q[3]), transl(dh_para[2][1],0,0))
#    T_4_5 = np.dot(rotz(q[4]), transl(dh_para[3][2],0,0))
#    T_5_6 = np.dot(rotz(q[5]), transl(dh_para[4][2],0,0))
#    #weil erstes Hilfskoordinatensystem ist sinds 7
#    T_6_7 = np.dot(rotz(q[]))
    
    #oder mit dh
    T_0_1 = dh(dh_para[0][0], dh_para[0][1], dh_para[0][2], q[0])
    #print("T01 = ", T_0_1)
    T_1_2 = dh(dh_para[1][0], dh_para[1][1], dh_para[1][2], q[1])
    #print("T02 = ", np.dot(T_0_1,T_1_2))
    T_2_3 = dh(dh_para[2][0], dh_para[2][1], dh_para[2][2], q[2])
    T_3_4 = dh(dh_para[3][0], dh_para[3][1], dh_para[3][2], q[3])
    T_4_5 = dh(dh_para[4][0], dh_para[4][1], dh_para[4][2], q[4])
    T_5_6 = dh(dh_para[5][0], dh_para[5][1], dh_para[5][2], q[5])
    
    T_0_6 = np.dot(np.dot(np.dot(np.dot(np.dot(T_0_1, T_1_2),T_2_3),T_3_4),T_4_5),T_5_6)

    print("T_0_6 fk= ",T_0_6)
    
    return T_0_6

def ik_ur(dh_para, tcp, sol):
    #Inverse Kinematics for UR type Robots
    # Rückwärtskinematik
    T_0_6 = rotvec_2_T(tcp)
    print("T_0_6 = ", T_0_6)

    #Achse 5 in 0
    O5_in_0 = np.dot(T_0_6, np.array([0, 0, -dh_para[5, 2], 1])) #skr4,S.17
    print("O5_in_0 = ", O5_in_0)
    # Winkel q1 
    #----------todo------------ nr 3,4,5
    O5_in_0_x = O5_in_0[0];
    O5_in_0_y = O5_in_0[1];
    print("O5_in_0_x = ",O5_in_0_x)
    print("O5_in_0_y = ", O5_in_0_y)
    
    alpha1 = np.arctan2(O5_in_0_y, O5_in_0_x)
    print("alpha1 (rad) = ", alpha1)
    
    R = np.sqrt(np.square(O5_in_0_x) + np.square(O5_in_0_y))
    
    l4 = dh_para[3][2]
    print ("l4 = ", l4)
    print("R = ", R)
    
    alpha2 = np.arccos(l4/R)
    print("alpha2 (rad) = " , alpha2)
    
    if (sol & 4 == 0):
        q1 = alpha1 + alpha2 + np.pi / 2
    else:
        q1 = alpha1 - alpha2 + np.pi / 2
    
    print("q1 = ", q1, " = ", np.degrees(q1))
    
    # Winkel q5
    #------------todo--------------
    s1 = np.sin(q1)
    c1 = np.cos(q1)

    l6 = dh_para[5][2]
    print("l6 = ",l6)
    q5 = np.arccos((O5_in_0_x*s1 - O5_in_0_y*c1 - l4)/l6) 
    
    if sol & 1:
        q5 = -q5
        
    print("q5 = ", q5, " = ", np.degrees(q5))
    
    #Winkel q6
    #------------todo---------------
    s5 = np.sin(q5)
    c5 = np.cos(q5)
    
    q6 = np.arctan2((-T_0_6[0,1]*s1 + T_0_6[1,1]*c1)/s5, (T_0_6[0,0]*s1 - T_0_6[1,0]*c1)/s5)
    print("q6 = ", q6, " = ", np.degrees(q6))

    #Ebenes Problem mit drei parallelen Achsen
    T_0_1 = dh(dh_para[0, 0], dh_para[0, 1], dh_para[0, 2], q1)
    T_4_5 = dh(dh_para[4, 0], dh_para[4, 1], dh_para[4, 2], q5)
    T_5_6 = dh(dh_para[5, 0], dh_para[5, 1], dh_para[5, 2], q6)
    T_4_6 = np.dot(T_4_5, T_5_6)
    T_6_4 = Tinv(T_4_6)
    T_1_0 = Tinv(T_0_1)
    T_1_4 = np.dot(np.dot(T_1_0, T_0_6), T_6_4)
    #90 Grad rotation zwischen 4 und 5 komkensieren
    T_1_4 = np.dot(T_1_4, rotx(-np.pi / 2))
    print("T_1_4: ", T_1_4)
    
    x_S = T_1_4[0,3]
    y_S = T_1_4[1,3]
    #z_S = T_1_4[2,3]
    print("x_S = ", x_S)
    print("y_S = ", y_S)
    #---------------------------------------------------laut prof
    # weil ich hier T_1_4 verwende?
    l1 = abs(dh_para[1,1])   # wäre l2
    l2 = abs(dh_para[2,1])   # wäre l3
    #------------------------------------------------------------
    #l1 = abs(dh_para[0][2])
    #l2 = abs(dh_para[1][1])
    print("l1 = ", l1)
    print("l2 = ", l2)
    


    # Winkel q3
    #-----------------------todo----------------
    cos_q3 = (np.square(x_S)+np.square(y_S)-np.square(l1)-np.square(l2))/(2*l1*l2)
    print("cos_q3 = " , cos_q3)
    q3 = np.arccos(cos_q3)
        
    if (sol & 2 == 0):
        q3 = q3
    else:
        q3 = -q3
    
    print("q3 = ", q3, " = ", np.degrees(q3))
    #Winkel q2
    #-------------------todo---------------
    x = x_S
    y = y_S
    beta = np.arctan2(y, x)
    psi = np.arccos((np.square(x)+np.square(y)-np.square(l1)-np.square(l2))/(2*l1*np.sqrt(np.square(x)+np.square(y))))
    
    if q3 > 0:
        q2= beta - psi - np.pi
    else:
        q2 = beta + psi - np.pi
        
    if q2 < -np.pi:
        q2 = q2 + 2 * np.pi
    
    print("q2 = ", q2, " = ", np.degrees(q2))
    #Gesamtwinkel
    q234 = 0 #---------------todo----------- ??????????????????
    
    #Winkel q4
    q4 = q234 - q2 - q3
    print("q4 = ", q4, " = ", np.degrees(q4))
    
    return np.array([q1, q2, q3, q4, q5, q6])
        




