import numpy as np

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
def traj_sample(qStart, qTarget, ts1, ts2, tges, a, v, delta_t): #mit a = neues amax und v = neues vmax

    #timestamp array
    t = np.arange(0, tges + delta_t, delta_t) 
    #initialize other variables in the size of t
    qt = np.zeros(t.size)
    vt = np.zeros(t.size)
    at = np.zeros(t.size)
    
    delta_q = qTarget - qStart

    # a und v umkehren wenn von großem Winkel zu kleinem gefahren wird
    if (qStart > qTarget):
        a = -a
        v = -v
        
    if(ts1 == ts2):
        # Dreieck
        print("Dreieck")
        
        qs = qStart + 0.5 * a * ts1**2
        vs = a * ts1
        
        i = 0
        for ti in t:
            
            if (ti < ts1):
                # steigend
                qt[i] = qStart + 0.5 * a * ti**2
                vt[i] = a * ti
                at[i] = a

            else:   
                # fallend
                qt[i] = qs + vs * (ti - ts1) - 0.5 * a * (ti - ts1)**2
                vt[i] = vs - a * (ti - ts1)
                at[i] = -a
            i = i+1
        
    else:
        # Trapez
        print("Trapez")
        
        qs1 = qStart + 0.5 * a * ts1**2
        #qs2 = delta_q - 1/2 * (v**2) / a 
        qs2 = qTarget - v**2 / (2 * a)

        print(0.5 * a * ts1**2)
        print(v**2 / (2 * a))
        print(qs1)
        print(qs2)
        
        i = 0
        for ti in t: 
            
            if (ti < ts1):
                # steigend
                qt[i] = qStart + 0.5 * a * ti**2
                vt[i] = a * ti
                at[i] = a
                
            elif (ti < ts2):
                # ebene
                qt[i] = qs1 + (ti-ts1) * v
                vt[i] = v
                at[i] = 0
                
            else:
                # fallend
                qt[i] = qs2 + (v + (a *delta_q) / v) * (ti -ts2) - 0.5 * a * (ti**2 - ts2**2)
                vt[i] = - a * ti + v + (a*delta_q) / v
                at[i] = -a 
            
            i = i + 1
    
    return[qt, vt, at, t]
    



    