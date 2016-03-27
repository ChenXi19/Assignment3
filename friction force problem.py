# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 10:22:03 2016

@author: 抽抽
"""

import numpy as np
import matplotlib.pyplot as plt


t=np.linspace(0,10,10)

def draw_pic(a,b,v0):
    a=float(a)
    b=float(b)
    v0=float(v0)
    v=[ ]
    dv=[ ]
    v.append(v0)
    
    for i in range(9):
        v_new = v[i]+(a-b*v[i])*t[1]
        v.append(v_new)
        
    V=(a/b)*(1-np.exp(-b*t))+v0*np.exp(-b*t)
        
    plt.figure(figsize=(10,10)) 
    plt.plot(t,V,label='exact solution',color='black',linewidth=1)
    plt.plot(t,v,label='Euler solution',color='red',linewidth=1,linestyle='--') 
    plt.legend()
    plt.show()  
    plt.xlabel('time(s)')
    plt.ylabel('velocity(m/s)')
    plt.title('Friction Force Problem')
    
    for j in range(9):
        det_v=v[j]-V[j]
        dv.append(det_v)
        
    print(max(dv))
    print(dv)
    
draw_pic(10,1,20)


        

        
    
    