# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 23:55:25 2020

@author: nightwolfer
"""


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider


'''
task 1 Set up function
'''

def pol_sin_deg2(x,omega=1,a=np.pi/2):
    
    '''
    Taylor expansion expanding on x
    #f(aw)+f'(aw)/1*(x-a) +f''(aw)/(1*2)*(x-a)**2
    a is where we center the approximation
    w is frequency 
    '''
    
   
    return np.sin(a*omega)+np.cos(a*omega)*(x-a)-1/2*np.sin(a*omega)*(x-a)**2 
    

x=np.linspace(0,2*np.pi,40)
#y_val=np.linspace(0,2*np.pi,40)
y1,y2=np.sin(x),pol_sin_deg2(x)



#Test plot where x0=a is pi/2 and y0=omega is pi/2

 
fig, ax =plt.subplots(figsize=(12,6))
ax.plot(x,y1,'red')
ax.plot(x,y2,'blue')#plotting with built in sin functiona
ax.legend(['Taylor polynomia approximation for sin(wx)x=0->2pi,w=1,x0=pi/2','Sin value for x=pi/2,w=pi/2'])

'''
Task 2 Design and program a GUI which serves as user friendly way to input ineractivly two parametes x0 and w to fast and easely 
vary the curves to demonstrate theire dependeces on this parameters
'''

#almost copypaste from code for two sliders in 11th lecture
y3=pol_sin_deg2
fig=plt.figure()
sldx_ax=plt.axes([0.1,0.5,0.3,0.03])
sldomega_ax=plt.axes([0.1,0.4,0.3,0.03])
ax=plt.axes([0.5,0.1,0.4,0.8])
x0=np.pi/2
omega0=1
sldx=Slider(sldx_ax,'x',0,2*np.pi,valinit=x0,valfmt="%1.2f")
sldomega=Slider(sldomega_ax,'omega',0,2*np.pi,valinit=omega0,valfmt="%1.2f")
x=np.linspace(0,2*np.pi,40)
line, =ax.plot(x,y3(x,sldomega.val,sldx.val))
ax.plot(x,y1,'r--',lw=3)
ax.legend(['Tayolor approximation with interactive centering point x and frequency w','Built in sinus function'])
ax.set_xlabel('x 0 -> 2pi')
ax.set_ylabel('sin(wx)')

def update_curve(val):
    line.set_ydata(y3(x,sldomega.val,sldx.val))
    
sldomega.on_changed(update_curve)
sldx.on_changed(update_curve)
plt.show()