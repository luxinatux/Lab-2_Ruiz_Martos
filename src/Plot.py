#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 15:10:00 2022

@author: dylanruiz
"""

import serial
from matplotlib import pyplot as plt

def plot():
    with serial.Serial ('COMx', 115200) as s_port:
        
        s_port.write(b,4) #runs the main function
        
        
        print(s_port.readline().split(b',')
        
              
              
              


 
                 
                
    #print(x_list)
    #print(y_list)

    #https://matplotlib.org/stable/tutorials/introductory/pyplot.html



    plt.plot(x_list,y_list)
    plt.xlabel("I Never Watched")
    plt.ylabel("Monty Python")