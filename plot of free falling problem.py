# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 11:05:57 2016

@author: 抽抽
"""

import numpy as np
import matplotlib.pyplot as plt

t=np.linspace(0,10,10)

def draw_pic(g,v0):
    g = float(g)
    v0 = float(v0)
    v=[]
    dv=[]
    v.append(v0)
    
    for i in range(9):
        v_new = v[i]-g*t[1]
        v.append(v_new)
   
    V = v0-g*t   
    
    plt.figure(figsize=(10,10)) 
    plt.plot(t,V,label='exact solution',color='black',linewidth=1)
    plt.plot(t,v,label='Euler solution',color='red',linewidth=3,linestyle='--') 
    plt.legend()
    plt.show()  
    plt.xlabel('time(s)')
    plt.ylabel('velocity(m/s)')
    plt.title('free falling problem')
    
    
    for j in range(9):
        det_v=v[j]-V[j]
        dv.append(abs(det_v))
        
    print(max(dv))
    
draw_pic(9.8,0)    
    
