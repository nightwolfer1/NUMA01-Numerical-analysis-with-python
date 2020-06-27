# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 11:50:35 2020

@author: nightwolfer
"""


import numpy as np
import matplotlib.pyplot as plt
import sys

#Task 1
x=0.5
a=0.5
x2=[0.5]

for i in range(1,200):
    x=np.sin(x2[i-1])-a*x2[i-1]+30
    x2.append(x)
    if np.abs(x2[i]-x2[i-1]) < 1.e-8:
        print('loop was executed untill index {index}'.format(index=int(i))) 
        break
    if i == 199:
        print('the break was never executed condition was not met.')
    
    
#Task 2
x=np.linspace(5,30,num=25)
 
plt.plot(x,x2[5:30])

#task 3

def funsin(n):
   return np.sin(n)**2/n

xnlist=[]

n=1
while np.abs(funsin(n)) > 1.e-9:
    xnlist.append(funsin(n))
    n=n+1
print('size of xn list is '+ str(len(xnlist)))  

#task 4  



def calc_conv(x,a):
    return 0.2*x-a*(x**2-5)

#initial value
xinit=1
xvalues=[xinit]
#gridpoint let check for 1000 a=-0.5, change a to the demand and controll if it converges.
v=1000
a=0.5
tick=0
for x in range(1,v):
    xn1=calc_conv(xvalues[x-1],a)
    xvalues.append(xn1)
    tick=x
    if np.abs(xn1-xvalues[x-1]) < 1.e-9:
        print('converged with value '+str(xvalues[-1])+'\n')
        for x in xvalues:
            if x<0:
                print('contained negative values')
                break
        break
        
if tick==999:
    print('did not converge, had a value '+str(a)+' last value on x =  ' + str(xvalues[-1]))       
    for x in xvalues:
            if x<0:
                print('contained negative values') 
                break
            
#task 5
#for a =0.5 contained positive and negative elements

def look_pos_neg(x):
    posl=[]
    negl=[]
    for num in x:
        if num >=0:
            posl.append(num)
        elif num < 0:
            negl.append(num)
    return (posl,negl)    

posl=look_pos_neg(xvalues)[0]
negl=look_pos_neg(xvalues)[1]



#task 6 & 7& 8

def calc_conv(x,a):
    return np.round(0.2*x-a*(x**2-5),7)

def fun_all(a,xinit):
    v=100
    
    #initial value
    xvalues=[xinit]
    #gridpoint let check for 1000 a=-0.5, change a to the demand and controll if it converges
    tick=0
    for x in range(1,v):
        xn1=calc_conv(xvalues[x-1],a)
        xvalues.append(xn1)
        tick=x
        if np.abs(xn1-xvalues[x-1]) < 1.e-9:
            print('converged with value '+str(xvalues[-1])+'\n')
            for x in xvalues:
                if x<0:
                    print('contained negative values')
                    break
            break
    posl=look_pos_neg(xvalues)[0]
    negl=look_pos_neg(xvalues)[1]            
    return (tick <= 30,posl,negl)
      
x=fun_all(0.25,2)
print(x[0])
print(x[1])
print(x[2]) 
    
