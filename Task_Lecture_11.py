# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 13:17:45 2020

@author: nightwolfer
"""


import numpy as np
import matplotlib.pyplot as plt

#All tasks 1-4
#sin approx by taylor expansion, for 2th degree, x0=pi/2
def pol_sin_deg2(x,a=np.pi/2):
    #taylor expansion to 2th degree is 
    #f(pi)+f'(pi)/1*(x-pi) +f''(pi)/(1*2)*(x-pi)**2
    '''
    x is the value at which we apporximate with taylos polynomial
    when x=a whe should get the correct approximation
    '''
    return np.sin(a)+np.cos(a)*(x-a)-np.sin(a)*(x-a)**2
#order 2 and degree 2 should be same i might have misunderstood.
def pol_sin_ord2(x,a=(3/(np.pi*2))):
    #taylor expansion to 2th degree is 
    #f(pi)+f'(pi)/1*(x-pi) +f''(pi)/(1*2)*(x-pi)**2
    '''
    x is the value at which we apporximate with taylos polynomial
    when x=a whe should get the correct approximation
    '''
    return np.sin(a)+np.cos(a)*(x-a)-np.sin(a)*(x-a)**2



#area green is where approximation function for 2th order a=3/2pi has a difference with real function that is less than 0.2
#area red is where approximation function for 2th degree a=pi/2 has a difference with real function that is less than 0.2
x=np.linspace(0,2*np.pi,40)

#Gona construct array where sin(x)- sin_approx(x)<0.2 for both cases a=pi/2 and a=3/2pi
Arr_deg2y=[]
xdeg2=[]
Arr_ord2y=[]
xord2=[]
p_deg2=[]
i=0
#Storing lists where the condition that the difference between sin and approximation is equal to or less then 0.2
#Also storing the position for where this happens in the 2thdeg fun where a=pi/2 needed when using fill function
#for order 2 approx this is not needed since indexing starts from 0 (concluded by looking at plot.) could have done same
for x in x:
    if np.abs(pol_sin_deg2(x)-np.sin(x)) <= 0.2:
        Arr_deg2y.append(pol_sin_deg2(x))
        xdeg2.append(x)
        p_deg2.append(i)
    if np.abs(pol_sin_ord2(x)-np.sin(x)) <= 0.2:
        Arr_ord2y.append(pol_sin_ord2(x))
        xord2.append(x)
        
    i+=1
x=np.linspace(0,2*np.pi,40)
y1,y2,y3=np.sin(x),Arr_deg2y,Arr_ord2y

fig, ax = plt.subplots(figsize=(8,6))
ax.plot(x,y1,color='red')
ax.plot(xdeg2,y2,color='green')
ax.plot(xord2,y3,color='black')
ax.fill_between(xdeg2,y1[p_deg2],y2, color='green', alpha=0.3)
ax.fill_between(xord2,y1[:len(xord2)],y3, color='red', alpha=0.3)
ax.set_xticks([0,(3/(np.pi*2)),np.pi/2])
ax.set_xticklabels(['$0$','$3/(2\pi)$','$\pi/2$'])
ax.set_yticks([0,np.sin(3/(np.pi*2)),np.sin(np.pi/2)])
ax.set_xticklabels(['$0$','$3/(2\pi)$','$\pi/2$'])
ax.annotate('Polynomial approx intersec for x=a,pi/2',xy=(np.pi/2,pol_sin_deg2(np.pi/2)),xytext=(np.pi/2-0.2,pol_sin_deg2(np.pi/2)+0.2),arrowprops=dict(facecolor='black',shrink=0.1))
ax.annotate('Polynomial approx intersec for x=a,3/(2*pi)',xy=(3/(np.pi*2),pol_sin_ord2(3/(np.pi*2))),xytext=(3/(np.pi*2)+0.2,pol_sin_ord2(3/(np.pi*2))+0.4),arrowprops=dict(facecolor='black',shrink=0.1))
ax.set_xlim([0,2.5])
ax.set_ylim([0,1.2])
ax.legend(['Sin','2DegreeApprox pi/2','2OrderApprox 3/2pi'])
