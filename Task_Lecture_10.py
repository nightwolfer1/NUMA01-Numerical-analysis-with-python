# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 10:50:46 2020

@author: nightwolfer
"""


import numpy as np
import matplotlib.pyplot as plt 
#Task 1
x_val=np.linspace(-10,10,100)
#make a list of resulting values of the polynomial x**3+x
y=list(map(lambda x:x**3+x , x_val))
#derivateive of pol 3x**2+1
dydx=list(map(lambda x:3*x**2+1,x_val))

fig,ax = plt.subplots()
ax.plot(x_val,y,'red')
ax.plot(x_val,dydx,'green')
ax.set_title('Task 1')


#Task 2
#insection point is when the function changes sign going from negative to positive. (cureve goes from concave to convex)
#this happens at x= 0 so lets plot  between -2 and 2
fig,ax2 = plt.subplots()
ax2.plot(x_val,y,'red')
ax2.plot(x_val,np.linspace(-0.2,0.2,100),ls='-.',lw=0.5, color='black')#Tankent
ax2.set_xlim([-2,2])
ax2.set_ylim([-20,20])
ax2.set_title('Task 2')

#Task 3,4,5,6,7,8 Doing the same for extreme values, chaging polynomial to contain extreme values
x_val2=np.linspace(-2,2,100)
#make a list of resulting values of the polynomial x**3-2x
y2=list(map(lambda x:x**3-2*x, x_val2))
#derivateive of pol 3x**2-2
dydx2=list(map(lambda x:3*x**2-2,x_val2))

fig,ax3 = plt.subplots()
ax3.plot(x_val2,y2,'red')
ax3.plot(x_val2,dydx2,'black',lw=4)
ax3.plot(x_val2[20:45],np.linspace(y2[29],y2[29],25),ls='-.',lw=0.5, color='black')
ax3.plot(x_val2[60:85],np.linspace(y2[70],y2[70],25),ls='-.',lw=0.5, color='black')
ax3.set_title('Task 3-8')
ax3.set_xticks([x_val2[29],0,x_val2[70]])
ax3.set_xticklabels([str(x_val2[29]),str(0),str(x_val2[70])])
ax3.annotate('local max',xy=(x_val2[29],y2[29]),xytext=(x_val2[29]+1,y2[29]+1),arrowprops=dict(facecolor='black',shrink=0.05))
ax3.annotate('local min',xy=(x_val2[70],y2[70]),xytext=(x_val2[70]+1,y2[70]+1),arrowprops=dict(facecolor='black',shrink=0.05))
#From regular plots we can se that one extreme value is around x=-0.7 and the other around x=0.7 
#search the local max at around -1,5 to 0
max_l_pos=np.array(y2[25:50]).argmax()+25
print(max_l_pos)# 29
min_r_pos=np.array(y2[55:80]).argmin()+55
print(min_r_pos)# 70
#Task 9
plt.savefig('Task_save.png')