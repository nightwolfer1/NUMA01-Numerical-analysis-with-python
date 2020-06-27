# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 21:56:20 2020

@author: nightwolfer
"""
import numpy as np
import matplotlib.pyplot as plt

#Task 1
#Angle from 0 ->  2 pi
xtert=np.linspace(0,2*np.pi,50)

def complex_val(terta,r):
    return r*np.exp(1j*terta)





#we can store plot 10 circles in complex plane with varying radius from 0.1 to 1
#real is the x values and imag is the y values of circle from eulers formula    
ra=np.linspace(0.1,1.0,10)
 
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')   
for r in ra: 
    circle=[complex_val(xtert,r) for xtert in xtert]
    zreal=[x.real for x in circle]
    zimag=[x.imag for x in circle]
    plt.plot(zreal,zimag,'black')











#Task 2 newtons method

#Derivative fun



def poly_fun(x):
    return x**2-5*x



def myfuncp(f,x,h=1e-5):
    """
    Newtons difference quotient
    Finite difference, two point estimate

    Parameters
    ----------
    f : function
        The function we want to derivate 
    x : int,float
        The the point for the derivative
    h : float, optional
        stepsize lim -> 0 is the derivative the smaller the closer to true derivative. The default is 1e-5.

    Returns
    -------
    Der_val : int,float
        returns the value of the derivative at point x.

    """
    
    Der_val=(f(x+h)-f(x))/h
    
    
    return Der_val


def myfunc(f,fp,x0,Tol=1e-3):
    """
    
    Newton method for finding root of function. 
    
    Parameters
    ----------
    f : function
        The function we want to find a root to.
    fp : function
        find the value of the derivative of the function at value x.
    x0 : int,float
        initial value
    Tol : float, optional
        Tolerance of the newton method. The default is 1e-3.

    Returns
    -------
    The root of f(x), f(x)=0, if newthon method dosent converge it returns False
    """
    n=400 #400 iterations
    x1=x0 #initial value
    conv=False
    for n in range(n):
        xnew=x1-(f(x1)/fp(f,x1))
        if np.abs(xnew-x1) < Tol:
            conv=True
            return (xnew,conv)
        else:
            x1=xnew
    else: return conv
    
a=myfunc(poly_fun,myfuncp,3)
b=myfunc(np.cos,myfuncp,3)