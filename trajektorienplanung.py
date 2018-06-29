import numpy as np
import importlib
import math
import libary_1 as robo
importlib.reload(robo)

"""
1. Berechnung der Schaltzeitpunkte
"""
def traj_timestamps(qStart, qTarget, amax, vmax):
    
    qgrenz = (vmax*vmax) / amax
    delta_q = abs(qTarget - qStart)
    
    
    if delta_q <= qgrenz:
        # --> Dreieck
        ts1 = np.sqrt(delta_q/amax)
        ts2 = ts1
        tges = 2 * ts1
    
    else:
        # --> Trapez
        tges = (delta_q/ vmax) + (vmax/amax)
        ts1 = vmax / amax
        ts2 = tges - ts1 
    
    return [ts1, ts2, tges]

"""
2. Berechnung der Beschleunigung und Geschwindigkeit 
    bei gegebenen Schaltzeitpunkten
"""
def traj_getav (qStart, qTarget, ts1, tges):
    delta_q = abs(qTarget-qStart)
    a = delta_q/(ts1*tges-ts1**2)       # a ist neues amax
    v = a * ts1                         # v ist neues vmax
    
    return [a, v]

"""
3. Abtastung der Trajektorie
"""
def traj_sample(qStart, qTarget, ts1, ts2, tges, amax, vmax, delta_t): 
    
    #timestamp array
    t = np.arange(0, tges + delta_t, delta_t) 
    #initialize other variables in the size of t
    qt = np.zeros(t.size)
    vt = np.zeros(t.size)
    at = np.zeros(t.size)
    
    delta_q = qTarget - qStart

    # a und v umkehren wenn von großem Winkel zu kleinem gefahren wird
    if (qStart > qTarget):
        amax = -amax
        vmax = -vmax
        
    if(ts1 == ts2):
        # Dreieck
        print("Dreieck")
        
        #q und v zum Schaltzeitpunkt
        qs = qStart + 0.5 * amax * ts1**2
        vs = amax * ts1
        
        i = 0
        for ti in t:
            
            if (ti < ts1):
                # steigend
                qt[i] = qStart + 0.5 * amax * ti**2
                vt[i] = amax * ti
                at[i] = amax

            else:   
                # fallend
                qt[i] = qs + vs * (ti - ts1) - 0.5 * amax * (ti - ts1)**2
                vt[i] = vs - amax * (ti - ts1)
                at[i] = -amax
            i = i+1
        
    else:
        # Trapez
        print("Trapez")
        
        qs1 = qStart + 0.5 * amax * ts1**2
        #qs2 = delta_q - 1/2 * (v**2) / a 
        qs2 = qTarget - vmax**2 / (2 * amax)
        
        i = 0
        for ti in t: 
            
            if (ti < ts1):
                # steigend
                qt[i] = qStart + 0.5 * amax * ti**2
                vt[i] = amax * ti
                at[i] = amax
                
            elif (ti < ts2):
                # ebene
                qt[i] = qs1 + (ti-ts1) * vmax
                vt[i] = vmax
                at[i] = 0
                
            else:
                # fallend
                qt[i] = qs2 + (vmax + (amax * delta_q) / vmax) * (ti -ts2) - 0.5 * amax * (ti**2 - ts2**2)
                vt[i] = -amax * ti + vmax + (amax * delta_q) / vmax
                at[i] = -amax
            
            i = i + 1
    
    return[qt, vt, at, t]
    
"""
Alle 6 Achsen
"""
def traj_6_axis(qStart, qTarget, vmax, amax):
        
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
        [ts1[i],ts2[i],tges[i]] = traj_timestamps(qStart[i], qTarget[i], amax, vmax)
        print("Achse",i+1," : ", "ts1= ", ts1[i],"ts2= ", ts2[i],"tges= ", tges[i])
        
        achse[i, 0:3] = [ts1[i],ts2[i],tges[i]]
        if  achse[i, 2] > tges_max:
            tges_max = achse[i, 2]
            i_lead_axis = i
                
    print("Führungsachse = Achse",i_lead_axis+1)
    
    for i in range(6):
        # neues a und v für alle Achsen außer Führungsachse
        [achse[i,3], achse[i,4]] = traj_getav(qStart[i], qTarget[i], ts1[i_lead_axis], tges[i_lead_axis])
        # ts1 ts2 tges der Führungsachse entsprechen jetzt den anderen bewegenden Achsen
        if achse[i, 2] != 0: #dann bewegt sich achse
            achse[i, 0] = achse[i_lead_axis, 0]
            achse[i, 1] = achse[i_lead_axis, 1]
            achse[i, 2] = achse[i_lead_axis, 2]  
        
    print("Achsen ts1, ts2, tges, a, v : ", "\n", achse)
    return achse

"""
get a v for movej with given time
"""
def movej_with_t_getav (qStart, qTarget, tges):
    if (abs(qTarget-qStart) < 1.5):
        # Dreieck 
        ts1 = tges/2
    else: 
        # Trapez
        ts1 = 0.25 * tges
 
    delta_q = abs(qTarget-qStart)
    a = delta_q/(ts1*tges-ts1**2)       # a ist neues amax
    v = a * ts1                         # v ist neues vmax
    
    return [a, v]
    
"""
4. Pose
"""
def traj_poseTimestamps (pStart, pTarget, vmax, amax):
        
    pgrenz = (vmax*vmax) / amax
    # Abstand der Punkte im Raum:
    delta_p = np.sqrt((pStart[0] - pTarget[0])**2 + (pStart[1] - pTarget[1])**2 + (pStart[2] - pTarget[2])**2)
    
    if delta_p <= pgrenz:
        # --> Dreieck
        ts1 = np.sqrt(delta_p / amax)
        ts2 = ts1
        tges = 2 * ts1
    
    else:
        # --> Trapez
        tges = (delta_p / vmax) + (vmax / amax)
        ts1 = vmax / amax
        ts2 = tges - ts1 
    
    return [ts1, ts2, tges]

    
def traj_poseSample (pStart, pTarget, vmax, amax, delta_t):
    
    [ts1, ts2, tges] =  traj_poseTimestamps(pStart, pTarget, vmax, amax)
    
    
    delta_p = np.sqrt((pStart[0] - pTarget[0])**2 + (pStart[1] - pTarget[1])**2 + (pStart[2] - pTarget[2])**2)
    orientation = pTarget[0:3] - pStart[0:3]
    gradient = orientation / delta_p
    
     
    #timestamp array
    t = np.arange(0, tges + delta_t, delta_t) 
    #initialize other variables in the size of t
    """
    pose = xyzrxryrz
    """
    pose_t = np.zeros([t.size, 6])
    pose_vt = np.zeros([t.size, 6])
    pose_at = np.zeros([t.size, 6])
    
    vt = np.zeros(t.size)
    at = np.zeros(t.size)
         
    if(ts1 == ts2):
        """ Dreieck """
        
        # xyz und v zum Schaltzeitpunkt
        xyz_ts = np.zeros(3)
        xyz_ts[0:3] = pStart[0:3] + 0.5 * amax * (ts1**2) * gradient
        vs = amax * ts1        
        
        i = 0
        for i in range(t.size):
            
            if (t[i] < ts1):
                # steigend
                pose_t[i, 0:3] = pStart[0:3] + 0.5 * amax * (ts1**2) * gradient   # Werte 0:3
                pose_t[i, 3:6] = pStart[3:6]

                pose_vt[i, 0:3] = amax * ts1 * gradient
                pose_at[i, 0:3] = amax * gradient
                
                vt[i] = amax * t[i]
                at[i] = amax

            else:   
                # fallend
                pose_t[i, 0:3] = xyz_ts[0:3] + (vs * (t[i] -ts1) - 0.5 * amax * (t[i] - ts1)**2) * gradient   # Werte 0:3
                pose_t[i, 3:6] = pStart[3:6]

                pose_vt[i, 0:3] = vs - amax * (t[i] - ts1) * gradient
                pose_at[i, 0:3] = - amax * gradient
                
                vt[i] = vs - amax * (t[i] - ts1)
                at[i] = -amax
        
    else:
        # Trapez
        print("Trapez")
        
        # Error handling
        if(np.abs(delta_p) < 0.0001):
            """ delta_p = 0 """
            for i in range(t.size):     
                pose_t[i,0:3] = pStart[0:3]
                pose_t[i,3:6] = pStart[3:6]
                vt[i] = 0
                at[i] = 0
                
        else:
            """ delta_p > 0 """
            xyz_ts1 = np.zeros(3)
            xyz_ts2 = np.zeros(3)
            xyz_ts1[0:3] = pStart[0:3] + 0.5 * amax * (ts1**2) * gradient
            xyz_ts2[0:3] = pTarget[0:3] - (vmax**2 / (2 * amax)) * gradient
            
        i = 0
        for i in range(t.size): 
            
            if (t[i] < ts1):
                # steigend
                pose_t[i, 0:3] = pStart[0:3] + (0.5 * amax * t[i]**2) * gradient   # Werte 0:3
                pose_t[i, 3:6] = pStart[3:6]

                pose_vt[i, 0:3] = amax * t[i] * gradient
                pose_at[i, 0:3] = amax * gradient
                
                vt[i] = amax * t[i]
                at[i] = amax
                
            elif (t[i] < ts2):
                # ebene
                
                pose_t[i, 0:3] = xyz_ts1[0:3] + ((t[i] - ts1) * vmax) * gradient   # Werte 0:3
                pose_t[i, 3:6] = pStart[3:6]

                pose_vt[i, 0:3] = vmax * gradient
                # pose_at[i, 0:3] = 0
                             
                vt[i] = vmax
                at[i] = 0
                
            else:
                # fallend
                pose_t[i, 0:3] = xyz_ts2[0:3] + ((vmax + (amax * delta_p) / vmax) * (t[i] -ts2) * gradient - 0.5 * amax * (t[i]**2 - ts2**2)) * gradient   
                pose_t[i, 3:6] = pStart[3:6]

                pose_vt[i, 0:3] = (-amax * t[i] + vmax + (amax * delta_p) / vmax) * gradient
                pose_at[i, 0:3] = -amax * gradient
                            
                vt[i] = -amax * t[i] + vmax + (amax * delta_p) / vmax
                at[i] = -amax
    
    return[pose_t, pose_vt, pose_at, vt, at, t]

"""
get q with ik
"""
def ik_pose(pose_t, dh_para, sol):
    
    q_t = np.zeros((pose_t.shape[0],6))

    
    i = 0
    for row in q_t:
        
        q_t[i,:] = robo.ik_ur(dh_para, pose_t[i,:], sol)
        i += 1
        
    return q_t

#def ik_pose(pStart, pTarget, vmax, amax, delta_t, dh_para):
#    
#    [pose_t, pose_vt, pose_at, t] = traj_poseSample(pStart, pTarget, vmax, amax, delta_t)
#    q_t = np.zeros((pose_t.shape))
#
#    sol = 6
#    
#    for t in range(pose_t.shape[0]):
#        print(pose_t[t,:])
#        q_t[t,:] = robo.ik_ur(dh_para, pose_t[t,:], sol)
#        #print(q_t[t,:])
#        
#
#        
#    return q_t
#    
#def traj_PoseTimestamps(pStart, pTarget, vMax, aMax):
#    
#    #norm = sqrt(x^2 + y^2 + z^2)
#    pDiff = math.sqrt((pStart[0] - pTarget[0])**2 + (pStart[1] - pTarget[1])**2 + (pStart[2] - pTarget[2])**2)
#    pGrenz = (vMax * vMax) / aMax
#    
#    if pDiff <= pGrenz:
#        #Dreieck: tS1 = tS2, tGes
#        tGes = math.sqrt((4 * pDiff) / aMax)
#        tS1 = tGes/2
#        tS2 = tS1
#		
#    else:
#        #Trapez: tS1, tS2, tGes
#        tGes = (vMax / aMax) + (pDiff / vMax)
#        tS1 = vMax / aMax
#        tS2 = tGes - tS1
#    
#    return [tS1, tS2, tGes]
#
#    
#def traj_samplePose(pStart, pTarget, vMax, aMax, tDelta):
#    
#    [tS1, tS2, tGes] =  traj_PoseTimestamps(pStart, pTarget, vMax, aMax)
#    
#    pDiff = np.sqrt((pStart[0] - pTarget[0])**2 + (pStart[1] - pTarget[1])**2 + (pStart[2] - pTarget[2])**2)
#    
#    direction = pTarget[0:3] - pStart[0:3]
#    length = np.sqrt((direction[0]**2) + (direction[1]**2) + (direction[2]**2))
#    gradient = direction / length
#    
#    """
#    x = 5
#    linEq = pStart[0:3] + x * gradient
#    print(linEq)
#    """
#    
#    t = np.arange(0, tGes + tDelta, tDelta)
#    xyzrxryrzT = np.zeros([t.size,6])
#    xyzrxryrzVT = np.zeros([t.size,6])
#    xyzrxryrzAT = np.zeros([t.size,6])
#    vT = np.zeros(t.size)
#    aT = np.zeros(t.size)
#    
#    if(tS1 == tS2):
#        print("Dreieck")
#        i=0
#        
#        #Paramter Zeitpunkt tS1
#        xyzrxryrzTs = np.zeros(3)
#        xyzrxryrzTs[0:3] = pStart[0:3] + 0.5 * aMax * (tS1**2) * gradient
#        vTs = aMax * tS1
#        #print(vTS)
#        #vTS = np.sqrt(aMax * qDiff)
#        #print(vTS)
#        
#        for i in range(t.size):
#            
#            if(t[i] < tS1):
#                #Dreieck steigend
#                xyzrxryrzT[i,0:3] = pStart[0:3] + 0.5 * aMax * (tS1**2) * gradient
#                xyzrxryrzT[i,3:6] = pStart[3:6]
#                
#                xyzrxryrzVT[i,0:3] = aMax * tS1 * gradient
#                xyzrxryrzAT[i,0:3] = aMax * gradient
#                
#                vT[i] = aMax * t[i]
#                aT[i] = aMax
#            else:
#                #Dreieck fallend
#                xyzrxryrzT[i,0:3] = xyzrxryrzTs[0:3] + (vTs * (t[i] - tS1) - 0.5 * aMax * ((t[i] - tS1)**2)) * gradient
#                xyzrxryrzT[i,3:6] = pStart[3:6]
#                
#                xyzrxryrzVT[i,0:3] = vTs - aMax * ((t[i] - tS1)) * gradient
#                xyzrxryrzAT[i,0:3] = - aMax * gradient
#                vT[i] = vTs - aMax * (t[i] - tS1) 
#                aT[i] = - aMax
#                
#        
#        #print(qT)
#        
#    else:
#        print("Trapez")
#        i = 0
#        
#        if(np.abs(pDiff) < 1e-4):
#            #qDiff == 0
#            
#            for i in range(t.size):     
#                xyzrxryrzT[i,0:3] = pStart[0:3]
#                xyzrxryrzT[i,3:6] = pStart[3:6]
#                vT[i] = 0
#                aT[i] = 0
#
#
#        else:
#            #qDiff > 0
#            xyzrxryrzTs1 = np.zeros(3)
#            xyzrxryrzTs2 = np.zeros(3)
#            xyzrxryrzTs1[0:3] = pStart[0:3] + 0.5 * aMax * (tS1**2) * gradient
#            xyzrxryrzTs2[0:3] = pTarget[0:3] - (vMax**2 / (2 * aMax)) * gradient
#        
#            #qTS1 = qStart + vMax**2 / (2 * aMax)
#            #qTS2 = qTS1 + (tS2 - tS1) * vMax
#        
#            #print(0.5 * aMax * tS1**2)
#            #print(vMax**2 / (2 * aMax))
#            #print(xyzrxryrzTs1[0:3])
#            #print(xyzrxryrzTs2[0:3])
#            
#            for i in range(t.size):
#                
#                if(t[i] < tS1):
#                    #Trapez steigend
#                    xyzrxryrzT[i,0:3] = pStart[0:3] + (0.5 * aMax * t[i]**2) * gradient
#                    xyzrxryrzT[i,3:6] = pStart[3:6]
#                    
#                    xyzrxryrzVT[i,0:3] =aMax * t[i] * gradient
#                    xyzrxryrzAT[i,0:3] = aMax * gradient
#                    
#                    vT[i] = aMax * t[i]
#                    aT[i] = aMax
#                    
#                elif(t[i] < tS2):
#                    #Trapez konst
#                    xyzrxryrzT[i,0:3] = xyzrxryrzTs1[0:3] + ((t[i] - tS1) * vMax) * gradient
#                    xyzrxryrzT[i,3:6] = pStart[3:6]
#                    
#                    xyzrxryrzVT[i,0:3] = vMax * gradient
#                    
#                    vT[i] = vMax
#                    aT[i] = 0
#                    
#                else:
#                    #Trapez fallend
#                    xyzrxryrzT[i,0:3] = xyzrxryrzTs2[0:3] + ((vMax + (aMax * pDiff)/ vMax) * (t[i] - tS2) * gradient  - 0.5 * aMax * (t[i]**2 - tS2**2)) * gradient
#                    xyzrxryrzT[i,3:6] = pStart[3:6]
#                    
#                    xyzrxryrzVT[i,0:3] = (vMax + ((aMax * pDiff)/ vMax)) * gradient - aMax * t[i] * gradient
#                    xyzrxryrzAT[i,0:3] = - aMax * gradient
#                    
#                    vT[i] = - aMax * t[i] + vMax + (aMax * pDiff) / vMax
#                    aT[i] = - aMax
#    
#        
#    return[xyzrxryrzT, xyzrxryrzVT, xyzrxryrzAT, vT, aT, t]
#
#def traj_sampleAxesIk(tcpT, dhParaUR3, sol):
#    
#    qT = np.zeros((tcpT.shape[0],6))
#    
#    print(tcpT.shape[0])
#    
#    """
#    for i in range(8):
#        try:
#            qT[i,:] = rl.ik_ur(dhParaUR3, tcpT[0,:],i)
#            print(qT[i,:])
#        except:
#                print("fail")
#    """
#    
#    
#    try:
#        for i in range(tcpT.shape[0]):
#            qT[i,:] = rl.ik_ur(dhParaUR3, tcpT[i,:],sol)
#            
#            #Korrektur movel_x400
#            q4 = qT[i,3]
#            if np.abs(q4) >= (np.pi):
#                q4 = q4 - np.pi
#            if np.abs(q4) >= (np.pi):
#                q4 = q4 - np.pi
#            qT[i,3] = q4
#            
#    except:
#        #print("Fail")
#        return 0
#        
#    
#    #qIK = rl.ik_ur(dhParaUR3, rotvecQ, sol)
#    #print("sol:", sol, qIK)
#    
#    return qT
    
    

    