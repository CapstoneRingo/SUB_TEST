# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 23:33:32 2018

@author: pizzaslayer
"""

from MachineLib import *
import matplotlib.pyplot as plt

t = Trays(Position(),Position(-400,0),10,100)

xin = [0]*50
yin = [0]*50

xout = [0]*50
yout = [0]*50

for i in range(50):
    ip = t.touchpads[i].inPosition
    op = t.touchpads[i].outPosition
    
    xin[i] = ip.X
    yin[i] = ip.Y
    xout[i] = op.X
    yout[i] = op.Y
    
plt.plot(xin,yin,'bo',xout,yout,'ro')
plt.axis([-450,200,-20,300])