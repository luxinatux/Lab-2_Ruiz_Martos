"""
    @file           Plot.py
    @brief          Data Acquisition file  
    @details        Communicates to the nucleo via serial port to collect step response data and plot it
    @author         Dylan Ruiz
    @author         Lucas Martos-Repath
"""
import serial
import time
import struct
from matplotlib import pyplot as plt

def plot():
    '''
        @brief                  Runs main.py file on the nucleo and collects data.     
        @details                Runs main.py file on the nucleo via serial port and collects time and location(ticks) data from a step response.
                                When running on a different computer, ensure that the correct com port number is changed.
    '''
    with serial.Serial('COM3', 115200) as s_port:
        joe = ''
        s_port.write(b'\x03') #runs the main function
        time.sleep(1)
        s_port.write(b'\x04') #runs the main function
        time.sleep(1)
        
        Gain = input('Enter a Gain Value:')
        
        try:
            idx = float(Gain)
            # Checks if input is an integer
        except:
            print('ENTER A Number!')
            # If input is not an integer, prompts user to enter a positive integer
            # Returns program back to the beginning of while loop
        else:
            pass
        
        #ba = bytearray(struct.pack("f", idx)) #gain convert to binary represent
        joe = bytearray('{:}\r'.format(Gain),'utf8') 
        #print(joe)
        s_port.write(joe)
        
        #time.sleep(2)
        #s_port.write(b'L1\r')
        mixed_output = s_port.readline().split(b',')
        print(mixed_output)
        final = len(mixed_output)
        
        #s_port.write(b'L1\r') #endline? 
        
        #bytearray('hi', 'utf8')
        #bytearray('hi\r', 'utf8')
    s_port.close() #This made our code the only consistent repeatable output
    x_list = []
    y_list = []
    state = 0
    for i in range(final):

        if state == 0:
            try: 
                pos_1 = int(mixed_output[i])
            except ValueError:
                Fault_1 = False
                pass
            else: 
                Fault_1 = True
            state = 1
            if Fault_1 == True:
                pos_fin = pos_1
            continue
                
        if state == 1:
            try: 
                tim_1 = int(mixed_output[i])
            except ValueError:
                Fault_2 = False
                pass
            else: 
                Fault_2 = True
            state = 0
            
            if Fault_2 == True and Fault_1 == True:
                tim_fin = tim_1
                x_list.append(tim_fin)
                y_list.append(pos_fin)
        
                
                
    #print(x_list)
    #print(y_list)

    #https://matplotlib.org/stable/tutorials/introductory/pyplot.html


    #plotting of the data commences here
    plt.plot(x_list,y_list)
    plt.xlabel("Time[ms]")
    plt.ylabel("Position[ticks]")
    plt.title("Step Response, Kp = 0.15") #title is changed for various plots

if __name__ == '__main__':
    plot()