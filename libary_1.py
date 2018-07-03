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
    
    b = np.arctan2(-T[2][0], np.sqrt(np.exp(T[0][0])+np.exp(T[1][0]))) #beta
    a = np.arctan2(T[1][0]/np.cos(b), T[0][0]/np.cos(b)) #alpha
    g = np.arctan2(T[2][1]/np.cos(b), T[2][2]/np.cos(b)) #gamma
    return np.array([g, b, a])

def rpy_2_T(xyzrpy):
	# roll pitch yaw to matrix 
   # roll(x, gamma) pitch(y, beta) yaw(z, alpha)
   
    x = xyzrpy[0]
    y = xyzrpy[1]
    z = xyzrpy[2]   
    g = xyzrpy[3]   #gamma,roll,x
    b = xyzrpy[4]   #beta,pitch,y
    a = xyzrpy[5]   #alpha,yaw,z
        
    R = np.eye(3)
    R = np.dot(rotz(a), np.dot(roty(y), rotx(g)))

    T = np.eye(4)
    # Rotation
    T[0:3,0:3] = R[0:3,0:3] 
    # Translation
    T[0,3] = x
    T[1,3] = y
    T[2,3] = z
    
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
    
    if np.abs(np.sin(theta)) < 0.000001:
        rx = 0
        ry = 0
        rz = 0
        
    else:        
        rx = (1/(2 * np.sin(theta))) * (R[2, 1] - R[1, 2]) * theta
        ry = (1/(2 * np.sin(theta))) * (R[0, 2] - R[2, 0]) * theta
        rz = (1/(2 * np.sin(theta))) * (R[1, 0] - R[0, 1]) * theta
      
    return np.array([x,y,z,rx,ry,rz])

 
def rotvec_2_T(xyzrxryrz):
    # rotation vector representation to matrix
    
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
    
    #Rotation
    theta = np.sqrt(np.square(rx) + np.square(ry) + np.square(rz))
    
    kx = rx/theta
    ky = ry/theta 
    kz = rz/theta

    st = np.sin(theta)
    ct = np.cos(theta)
    vt = 1 - ct

    #Spalte 1
    T[0,0] = kx * kx * vt + ct
    T[1,0] = kx * ky * vt + kz * st
    T[2,0] = kx * kz * vt -ky * st
    #Spalte 2
    T[0,1] = kx * ky * vt - kz * st
    T[1,1] = ky * ky * vt + ct
    T[2,1] = ky * kz * vt + kx * st
    #Spalte 3
    T[0,2] = kx * kz * vt + ky * st
    T[1,2] = ky * kz * vt - kx * st
    T[2,2] = kz * kz * vt + ct

    
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
#forward Kinematics for UR type robots

    T_0_1 = dh(dh_para[0][0], dh_para[0][1], dh_para[0][2], q[0])
    T_1_2 = dh(dh_para[1][0], dh_para[1][1], dh_para[1][2], q[1])
    T_2_3 = dh(dh_para[2][0], dh_para[2][1], dh_para[2][2], q[2])
    T_3_4 = dh(dh_para[3][0], dh_para[3][1], dh_para[3][2], q[3])
    T_4_5 = dh(dh_para[4][0], dh_para[4][1], dh_para[4][2], q[4])
    T_5_6 = dh(dh_para[5][0], dh_para[5][1], dh_para[5][2], q[5])
    
    T_0_6 = np.dot(np.dot(np.dot(np.dot(np.dot(T_0_1, T_1_2),T_2_3),T_3_4),T_4_5),T_5_6)
    
    return T_0_6

def ik_ur(dh_para, tcp, sol):
    #Inverse Kinematics for UR type Robots

    T_0_6 = rotvec_2_T(tcp)

    #Achse 5 in 0
    O5_in_0 = np.dot(T_0_6, np.array([0, 0, -dh_para[5, 2], 1])) #skr4,S.17
    
    """
    Winkel q1
    """
    O5_in_0_x = O5_in_0[0];
    O5_in_0_y = O5_in_0[1];
    
    alpha1 = np.arctan2(O5_in_0_y, O5_in_0_x)
    
    R = np.sqrt(O5_in_0_x**2 + O5_in_0_y**2)

    l4 = abs(dh_para[3, 2])
    
    alpha2 = np.arccos(l4/R)
    
    if (sol & 4 == 0):
        q1 = alpha1 + alpha2 + np.pi / 2
    else:
        q1 = alpha1 - alpha2 + np.pi / 2
        
    """
    Winkel q5
    """
    s1 = np.sin(q1)
    c1 = np.cos(q1)

    l6 = abs(dh_para[5,2])
    q5 = np.arccos((T_0_6[0,3]*s1 - T_0_6[1,3]*c1 - l4)/l6) 
    
    if sol & 1:
        q5 = -q5
            
    """
    Winkel q6 
    """
    s5 = np.sin(q5)
    #c5 = np.cos(q5)
    
    #Ebenes Problem mit drei parallelen Achsen
    T_0_1 = dh(dh_para[0, 0], dh_para[0, 1], dh_para[0, 2], q1)
    T_1_0 = Tinv(T_0_1)
    T_1_6 = np.dot(T_1_0, T_0_6)
    
    q6 = np.arctan2((-T_1_6[1,2]/s5),(T_1_6[0,2]/s5))

    T_4_5 = dh(dh_para[4, 0], dh_para[4, 1], dh_para[4, 2], q5)
    T_5_6 = dh(dh_para[5, 0], dh_para[5, 1], dh_para[5, 2], q6)
    T_4_6 = np.dot(T_4_5, T_5_6)
    T_6_4 = Tinv(T_4_6)
    T_1_4 = np.dot(np.dot(T_1_0, T_0_6), T_6_4)
    T_1_4 = np.dot(T_1_4, rotx(-np.pi / 2))
    
    x_S = T_1_4[0,3]
    y_S = T_1_4[1,3]

    # weil hier T_1_4 
    l1 = abs(dh_para[1,1])   
    l2 = abs(dh_para[2,1])       

    """
    Winkel q3
    """
    cos_q3 = (np.square(x_S)+np.square(y_S)-np.square(l1)-np.square(l2))/(2*l1*l2)
    # handle NAN q3
    if cos_q3 > 1: #
        cos_q3 = np.round(cos_q3, decimals=0)
        
    q3 = np.arccos(cos_q3)
        
    if (sol & 2 == 0):
        q3 = q3
    else:
        q3 = -q3
        
    """
    Winkel q2
    """
    x = x_S
    y = y_S
    beta = np.arctan2(y, x)
    psi = np.arccos((np.square(x) + np.square(y) + np.square(l1) - np.square(l2) ) / (2 * l1 * np.sqrt(np.square(x) + np.square(y))))
    if q3 > 0:
        q2= beta - psi - np.pi
    else:
        q2 = beta + psi - np.pi
        
    if q2 < -np.pi:
        q2 = q2 + 2 * np.pi
        
    """
    Gesamtwinkel
    """
    rotvec = T_2_rotvec(T_1_4)
    q234 = rotvec[5]
    
    """
    Winkel q4
    """
    q4 = q234 - q2 - q3
    
    return np.array([q1, q2, q3, q4, q5, q6])


