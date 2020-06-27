# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 12:13:10 2020

@author: nightwolfer
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad

#task 1
#omega is 2pi, function integrated between 0 and pi/2
def  make_sin(x,omega=2*np.pi):
    
    return np.sin(omega*x)
   

result=quad(make_sin,0,np.pi/2)

#task 2
omega_array=np.linspace(0,2*np.pi,num=1000)


def  make_sin(omega):
    def f(x):
        return np.sin(omega*x)
    return f
    




y=[quad(make_sin(x),0,np.pi/2)[0] for x in omega_array ]

plt.plot(omega_array,y,'red')
plt.title('integral of sin(omega*x) at x between 0 and pi/2')
plt.xlabel('omega')
plt.ylabel('itegral of sin at omega between 0 and pi/2 ')


#task 3
from scipy.optimize import fsolve
def poly(x):
    return x**2+x-3

#initial value 1
x0=1
result = fsolve(poly,x0)

#Task 4
def poly_a(a):
    def f(x):
        return a*x**2+x-3
    return f
#computing 20 values
#same initial value
fig =plt.figure()
ax=plt.subplot(1,1,1)
a_array=np.linspace(1,5,20) #x value of plot
ynew=[fsolve(poly_a(a),x0) for a in a_array]
ax.plot(a_array,ynew,'red')
plt.xlabel('a')
plt.ylabel('x value for f(x,a)=0')
#there is no linear dependency on a and zero
