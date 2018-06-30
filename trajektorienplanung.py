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
