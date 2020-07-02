# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 20:05:37 2020

@author: nightwolfer
"""
import numpy as np
import matplotlib.pyplot as plt
class PolyGon:
    def __init__(self,list_arr):
        
        if not isinstance(list_arr,list):
            raise TypeError('Must be a list with arrays containing corners of polygon')
        self.list_arr=list_arr 
        
        
        
        
    def plot_fun(self):
        templistclosed=self.list_arr[::]#making copy
        templistclosed.append(self.list_arr[0])#closing loop by adding first cornerpoint
        x, y=zip(*templistclosed) #making separate arrays one for x values and one for y values 
        plt.plot(x,y,'red')
        
class Rectangle(PolyGon):
    def __init__(self,list_arr):
        
        PolyGon.__init__(self,list_arr)
        self._A=list_arr[0]
        self._B=list_arr[1]
        self._C=list_arr[2]
        self._D=list_arr[3]
        self._a=self.A-self.B
        self._b=self.B-self.C
        self._c=self.C-self.D
        self._d=self.D-self.A
        
    def area(self):
        return np.abs(np.cross(self._a,self._b))
    
    def set_A(self,A):
        self._A=A
        self._a=self.A-self.B
        self._d=self.D-self.A
        
    def get_A(self):
        return self._A

    
    
    def set_B(self,B):
        self._B=B
        self._a=self.A-self.B
        self._b=self.B-self.C
        
        
    def get_B(self):
        return self._B

    def set_C(self,C):
        self._C=C
        self._b=self.B-self.C
        self._c=self.C-self.D
        
        
    def get_C(self):
        return self._C
    
    
    def set_D(self,D):
        self._D=D
        self._c=self.C-self.D
        self._d=self.D-self.A
        
        
    def get_D(self):
        return self._D
    
    
    
    
    
    def del_pt(self):
        raise Exception ('Dont delete this value')


    A=property(fget=get_A,fset=set_A,fdel=del_pt)
    B=property(fget=get_B,fset=set_B,fdel=del_pt)
    C=property(fget=get_C,fset=set_C,fdel=del_pt)
    D=property(fget=get_D,fset=set_D,fdel=del_pt)


class SpecialRectangle(Rectangle):
    def __init__(self,list_arr):
        Rectangle.__init__(self,list_arr)
        
    def __contains__(self,RectangleB):
        # SpecialRectangle are rectangle parallel to axis in first quadrant (x and y >=0)
        # to make sure one rectangle is within the other all points
        
        #checking that all the points are concurrent with corners for a rectangle within another. A->D goes clockwise
        array_to_check=[]
        array_to_check.append(np.array(self.A <= RectangleB.A))
        array_to_check.append(np.array(self.B[0] <= RectangleB.B[0])) #first array[0] is the x value of points
        array_to_check.append(np.array(self.B[1] >= RectangleB.B[1])) #second array[1] is the y value of points
        array_to_check.append(np.array(self.C >= RectangleB.C)) 
        array_to_check.append(np.array(self.D[0] >= RectangleB.D[0])) 
        array_to_check.append(np.array(self.D[1] <= RectangleB.D[1])) 
        array_to_check=np.array(array_to_check) #make it an array instead of list
        check=True
        for  corner in array_to_check:
            if not corner.all():
                check=False
            
        return check
        
        