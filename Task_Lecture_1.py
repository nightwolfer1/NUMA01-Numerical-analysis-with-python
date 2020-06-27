# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt
import sys


#task 2
f=2.3**2+0.25*2.3-5.0
print('expression is not zero with x=2.3 but instead ' +str(f))

#task 3 
L=[1,2]
L3= 3*L
print(L3[0])
print(L3[-1])

#L3[10] list index out of range


#task 4
L4=[k**2 for k in L3] # its a list comprehension that squares each element in the list L3
print(L4);

#task 5
L5=L3+L4
print(L5)

#task 6
k=[]
[k.append(x/100) for x in range(101)]
print(len(k))


#task 7
# its a for-loop that iterates between index 0->499.
#it makes s equal to [s-1] +1 for each loop where [s-1] is
#index
s=0
for i in range(0,500):
    s=s+1
print(s)

#in the second one it iterates between index 1->499 and it appends
#(adds a value) to the list for each iteration were the value is 
#the previouse value + the current index value.
#i index is 499 in the last iteration
ss=[0]
for i in range(1,500):
    ss.append(ss[i-1]+i)
print(str(ss[-1])+' '+str(s))

#task 8
xplot=[0]
for i in range(1,101):
    xplot.append(i/100)
print(xplot)

#task 9+10
yplot=np.arctan(xplot)
plt.plot(xplot,yplot)
plt.show()

#task 11

computed_sum =np.sum([1/np.sqrt(i) for i in np.asarray(range(1,201))]) 

#task 12
n=range(3,1001)
h=1/1000
a=-0.5
u=[np.exp(0),np.exp(h*a),np.exp(2*h*a)]

for n in range (3,1001):
    un=u[n-1]+h*a*(23/12*u[n-1]-4/3*u[n-2]+5/12*u[n-3])
    u.append(un)

x=range(0,1001)
td=[]
[td.append(k*h) for k in x]

plt.plot(td,u,'r--')


unew=[]
for n in range(0,len(td)):
    unew.append(np.abs(np.exp(a*td[n])-u[n]))

fig,axes =plt.subplots(nrows=1,ncols=2)
axes[0].plot(td,u)
axes[0].set_ylabel('u')
axes[1].plot(td,unew)


