# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 09:30:24 2020

@author: nightwolfer
"""
import numpy as np
import matplotlib.pyplot as plt
#Task 1
L=[0,1,2,1,0,-1,-2,-1,0]
L[0] #first indeces in list (first value in ordered list)
L[-1] #Last indeces
L[:-1] #every value until the last indecis not including last indeces
L+L[1:-1]+L #makes one list with in order of assignment the list that is sliced will not have first and last value
L[2:2]=[-3] # The list is assigned new in the 2th indeces with value -3
L[3:4]=[] # removes value in indece 3 (4th value since it assigns no value)
L[2:5]=[-5] #assign new values -5 to list between indeces 2->5 since assigned list has only one value two
#of the current values are removed.


#Task 2
# def f(x):
#     return np.sin(x)

#Does this work?
# x=3.
# #print(f()) #no argument is given to function x, shouldent work.
# #print(f) prints f object
# y=2*np.pi 
# print(f(y))  #This will work, the argument is y, and is independent on the variable name.

#Task 3
# def f(m):
#     L=[n-m/2 for n in range(m)]
#     return 1+L[0]+1
# # #i could instead of using list comprehension  use regular forloop
# # def f2(m):
# #     L=[]
# #     for n in range(m):
# #         L.append(n-m/2)
# #     return 1+L[0]+1    
    
# # print(str(f(7))+' is it same as '+ str(f2(7)))

# #operand // willround to the closest lower integer 3//2 =1.
# def f3(m):
#     L=[n-m//2 for n in range(m)]
#     return 1+L[0]+1

# print(str(f(7))+' is not same as '+ str(f3(7)))

#task 4.

Distance=[[0,20,30,40],[20,0,50,60],[30,50,0,70],[40,60,70,0]]
Redistance=[]
temp=[]
for i in range(len(Distance)):
    if len (temp) >0:
        Redistance.append(temp)
        temp=[]
    for k in range(len(Distance[0])):
        if Distance[i][k]==0:
            break
        else:temp.append(Distance[i][k])
else:Redistance.append(temp)

#with list comprehension
Redistance2=[]
[Redistance2.append(Distance[k][:k]) for k in range(1,len(Distance))]


#Task 5 
# / == Rel complement, Union is adding a set, and intersection is looking for somthing to remove
a=fruitbasketA=set(['apple','pear','banana'])
b=fruitbasketB=set(['apple','plum','kiwi'])
def symmetric_diff(a,b):
    return (a-b).union((b-a))
#same result as a.symmetric_difference(b)
    

#task 6
# Update method for set will union itself to other sets in argument (adding set objects not in eachothers set)
#intersection_update will update a set with the intersection of itself and another (removing all set objects not in each others set)
#intersection method will spit out the  common set objects in the sets controlling.

#task 7 & 8 & 9

def poly(x):
    return 3*(x**2)-5


    
def bisec(intv,f,tol=0.0001):
    
    a=intv[0]
    b=intv[1]
    print(str(a)+' a '+ str(b)+' b ')
    midpoint=(a+b)/2
    if np.abs((a-b)) <= tol:
        return ([a,b],midpoint)
    if f(a)*f(midpoint) < 0:
        b=midpoint
        return bisec([a,midpoint],f,tol)
    else:
        a=midpoint
        return bisec([midpoint,b],f,tol)
        


# for poly 
# x=np.linspace(-1.5,-0.40,num=50)
# y=[]
# [y.append(poly(x)) for x in x]
# k=bisec([-1.5,-0.4],poly)

# plt.plot(x,y)
# plt.plot(k[1],poly(k[1]),'*')
# plt.show()

#for arctan
# x=np.linspace(-0.5,0.6,num=50)
# y=[]
# [y.append(np.arctan(x)) for x in x]
# k=bisec([-0.5,0.6],np.arctan)

# plt.plot(x,y)
# plt.plot(k[1],np.arctan(k[1]),'*')
# plt.show()