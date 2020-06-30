# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 20:22:23 2020

@author: nightwolfer
"""


import numpy as np
import scipy as sp
import matplotlib.pyplot as plt


#Task 1 
class ComplexNumber:
    def __init__(self,other):
        self.real=other.real
        self.imag=other.imag
        
#task 2        
    def addition(self,add):
        
        return self.number+add
    
    def division(self,denom):
        return self.number/denom
    
    
    def multiplication(self,faktor):
        return self.number*faktor
    
    
    def power_complex(self,power):
        return self.number**power
    
    def Real(self):
        return self.number.Real
    
    def Imagi(self):
        return self.number.Imagi
    
    def is_imaginary(self,other):
        '''
        

        Parameters
        ----------
        other : TYPE
            DESCRIPTION.

        Returns
        -------
        boolean
            Return True if number is Imaginary

        '''
        return isinstance(other,complex)
    
    def is_real(self,other):
        '''
        

        Parameters
        ----------
        other : TYPE
            DESCRIPTION.

        Returns
        -------
        boolean
            Return True if number is Real

        '''
        return not isinstance(other,complex)
        
    
    
    

    
    
    def __call__(self):
        return self.number
    
    def complex_arg_abs(self):
        '''
        

        Returns
        -------
        tuple
            (arg(z),absolute_value(z))

        '''
        if self.real>0:
            return (np.arctan(self.imag/self.real),np.sqrt(self.imag**2+self.real**2))
        elif self.real <0 and self.imag >=0:
            
            return (np.arctan(self.imag/self.real)+np.pi,np.sqrt(self.imag**2+self.real**2))
        elif self.real <0 and self.imag <0:
            
            return (np.arctan(self.imag/self.real) -np.pi,np.sqrt(self.imag**2+self.real**2))
        elif self.real==0 and self.imag >0:
            
            return (np.pi/2,np.sqrt(self.imag**2+self.real**2))
        elif self.real==0 and self.imag <0:
            
            return (-np.pi/2,np.sqrt(self.imag**2+self.real**2))
        
        return "indetermined"
    
    def same_complex(self,other):
        '''
        

        Returns
        -------
        
            return true if complex numbers are equal

        '''
        return self.real==other.real and self.imag==other.imag
    
    def add_float(self,other):
        '''
    

        Returns
        -------
        Complex number
            Method adds float or complex number to complex number
            will not make number inplace.

        '''
        if isinstance(other,float):
            p=float(self.real)+float(other.real)
            
            return ComplexNumber(p+1j*self.imag)
        elif isinstance(other,complex):
            p=float(self.real)+float(other.real)
            a=float(self.imag)+float(other.imag)
            return ComplexNumber(p+1j*a)
        else:
            raise TypeError('Has to be float or Complex Number')
        

    def __repr__(self):
        return f'{self.real} + i{self.imag}'
            