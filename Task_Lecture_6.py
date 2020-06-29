# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 08:57:50 2020

@author: nightwolfer
"""

import numpy as np
from scipy.linalg import solve


Skew_var=np.array([[0,2,-45],[-2,0,-4],[45,4,0]])
ort_a=np.array([1,2])
ort_b=np.array([2,-1])

#Task 1
def is_symmetric(M):
    
    if M.shape[0] == M.shape[1]:
        if (M.T==-M).all():
            return -1
        else: 
            return 1
        
        
    return 0
  
      

#Task 2

def ort_check(a,b):
     '''
    

    Parameters
    ----------
    a : Array
        Vector for checking orthogonal
    b : Aray
        Vector for checking orthogonal

    Returns
    -------
    Boolean
        True if a & b are ortegonal, which will be true if dot product is 0

    '''
     return a@b==0


#Task 3
from scipy.linalg import norm
#normalised using scipy
def norm_vec_sci(a):
    return a/norm(a)
#normalizing manually
def norm_vec(a):
    '''
    To normalize the vector is the vector divided by absolute value of dot prod.
    
    '''


    return a/np.sqrt(a@a)
    
# Task 4   

def rot_matrix(a):
    '''
    

    Parameters
    ----------
    a : int,float
        Rotation angle

    Returns
    -------
    Matrix
        returns 2D rotation matrix with angle a.

    '''
    return np.array([[np.cos(a),np.sin(a)],[-np.sin(a),np.cos(a)]])

# To show that the inverse of a rotation matrix is the transpose, we can take dot product
# of transport and if it gives use true than we know that this is correct.

a_array=np.linspace(0,90,20)
#we will prove it buy varying the angle
Control =[rot_matrix(a)@rot_matrix(a).T for a in a_array] #should give us an array with 
# eye matrixes, based on 20 different a values
#print(Control) # as can be seen you get an array of identity matrixes, Therefor its true.

# Task 5
from scipy.linalg import eig
#contruct a 20 x 20 matrix
#constructed a 20x20 matrix with diagonal 4, sub and super diagonal 1.
v=np.zeros(400).reshape(20,20)
rng=np.arange(20)
rng1=np.arange(19)

v[rng,rng]=np.ones(20)*4
v[rng1, rng1+1]=np.ones(19)
v[rng1+1,rng1]=np.ones(19)

#Eigenvalue
[eigenvalue, eigenvector]=eig(v)

print(str(eigenvalue) + '\n') #eigenvalue of matrix


#task 6
k=v[::]
k[rng,rng]=np.ones(20)*4
k[rng1, rng1+1]=np.ones(19)
k[rng1+1,rng1]=-np.ones(19)
#eigenvalue for matrix with subdiagonal -1 superdiagonal 1 and diagonal 4
[eigenvalue2, eigenvector2]=eig(k)
print(str(eigenvalue2))
#not remember much about eigenvalues but seems to contain a imaginary part on eigenvalue.