#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 13:41:08 2022

@author: dylanruiz
"""

import motor_Ruiz_Martos
import encoder_Ruiz_Martos
import closedloop
import time
import pyb


def main(Gain):
        enableA = pyb.Pin(pyb.Pin.cpu.A10, pyb.Pin.OUT_PP)
        in1_mot = pyb.Pin(pyb.Pin.cpu.B4)
        in2_mot = pyb.Pin(pyb.Pin.cpu.B5)
        motor1 = motor_Ruiz_Martos.Motor(enableA,in1_mot,in2_mot,3) # motor in A
        motor1.enable()
        in1_enc = pyb.Pin(pyb.Pin.cpu.B6)
        in2_enc = pyb.Pin(pyb.Pin.cpu.B7)
        encoder1 = encoder_Ruiz_Martos.Encoder(in1_enc,in2_enc,4) # motor in A
        Closed_loop = closedloop.ClosedLoop(Gain, 0)
        time_start = time.ticks_ms()
        time_period = 10
        step = 4000
        time_next = 0
        while True:
            time_now = time.ticks_diff(time.ticks_ms(),time_start)
            if time_now >= time_next:
                time_next = time.ticks_add(time_next,time_period)
                encoder1.update()
                motor1.set_duty(Closed_loop.update(step,encoder1.get_position(),time_now))
            
            if time_now >= 1000:
                Closed_loop.print_lists()
                break
               
                
if __name__ == '__main__':
    while True:
        Gain = input('Enter a Gain Value:')
        try:
            idx = float(Gain)
            # Checks if input is an integer
        except:
            print('ENTER A Number!')
            # If input is not an integer, prompts user to enter a positive integer
            continue
            # Returns program back to the beginning of while loop
        else:
            pass
        # If input is an integer, program continues to check if it is a negative number
        main(idx)
        
        
        """TRYING TO get serial port stuff working"""
        


