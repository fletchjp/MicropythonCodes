# UART example using RS485 output for uart0
# This now works with the output from an Arduino  RS485
# It needs to work with the second HAT to translate RS485 at both ends.

from machine import UART, Pin
import time

#uart1 = UART(1, baudrate=9600, tx=Pin(8), rx=Pin(9))

uart0 = UART(0, baudrate=115200, tx=Pin(0), rx=Pin(1))
#txData = b'hello world\n\r'
#uart1.write(txData)
#time.sleep(1)
print ("Starting RS485 test program for input\n")
rxData = bytes()
while 1:
    while uart0.any() > 0:
        rxData = uart0.readline()
        print(rxData)
        #print(rxData.decode('utf-8'))

# output is b'\xff' whether using read or readline.