# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 20:57:36 2020

@author: nightwolfer
"""
import numpy as np
import datetime as dt 
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

#Task 1 Read the dates and the energy-Values form the file kwh.dat

myfile=open('kwh.dat','r')
myfile.readline()

yearmonthly=[]
kwh=[]


for line in myfile.readlines():
    date, energy = line.split()
    energy=int(energy)
    yearmonthly.append(date)
    kwh.append(energy)
#task 2 reversing list using internal method of lists.
kwh.reverse()
yearmonthly.reverse()
#Task 3
#Compute monthly energy consumtion from the data
#converting kwh to array internally and outside
kwh=[np.array(energy) for energy in kwh]
#using diff on kwh xn+1-xn for all arrays
kwh_diff=np.diff(kwh)
#Remove first date in yearmonthly since we are looking at consumption and first month is not included in that data
Monthly_consumption=yearmonthly[1:]
#Making a datime object of dates
Monthly_consumption=[dt.datetime.strptime(Consumption,'%Y-%m-%d') for Consumption in Monthly_consumption]
#Task 4 ploting data for montly consumption
fig, ax=plt.subplots(figsize=(20,12))
ax.plot(Monthly_consumption,kwh_diff)
ax.set_xticks(Monthly_consumption)
monthyearFmt = mdates.DateFormatter('%Y-%m')
ax.xaxis.set_major_formatter(monthyearFmt)
_ = plt.xticks(rotation=90)



#Task 5 Determin the moth with largest and smallest energy consumption.
#first make kwh np array
kwh=np.array(kwh)
Smallest_pos1=kwh.argmin()
Biggest_pos1=kwh.argmax()
Date_smallest_consumption=yearmonthly[Smallest_pos1]
Date_Biggest_consumption=yearmonthly[Biggest_pos1]
print(str(Date_smallest_consumption)+' is date for smallest consumption in  amount kwh is  ' +str(kwh[Smallest_pos1])+'\n')
print(str(Date_Biggest_consumption)+'  is date for biggest consumption in  amount kwh is ' +str(kwh[Biggest_pos1])+'\n')

#Task 6
#Determine in python the month with the largest and one with the smalles consumption
Smallest_pos2=kwh_diff.argmin()
Biggest_pos2=kwh_diff.argmax()
Date_smallest_consumption=Monthly_consumption[Smallest_pos2]
Date_Biggest_consumption=Monthly_consumption[Biggest_pos2]
print(str(Date_smallest_consumption)+' is date for smallest increase in consumption per month  kwh is  ' +str(kwh_diff[Smallest_pos2])+'\n')
print(str(Date_Biggest_consumption)+'  is date for biggest increase in consumption per month kwh is ' +str(kwh_diff[Biggest_pos2]))

#Task 7&8 mean value of energy consption
mean_consumption=np.mean(kwh)
print('mean consumption is '+ str(mean_consumption))

