import serial
import time
import struct


#from matplotlib import pyplot as plt

def plot():
    with serial.Serial('COM3', 115200) as s_port:
        joe = ''
        s_port.write(b'\x03') #runs the main function
        time.sleep(1)
        s_port.write(b'\x04') #runs the main function
        time.sleep(1)
        #print (s_port.readline().split (b','))
        Gain = input('Enter a Gain Value:')
        #Gain = 0.5
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
        print(int(mixed_output[2]))
        
        #s_port.write(b'L1\r') #endline? 
        
        #bytearray('hi', 'utf8')
        #bytearray('hi\r', 'utf8')
    s_port.close()

if __name__ == '__main__':
    plot()