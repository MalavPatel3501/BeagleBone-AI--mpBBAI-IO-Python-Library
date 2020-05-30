#/**************************************************************************************/
#/*File : mpBBAI-UART3.py                                                                */
#/*Made by: Malav Patel                                                                */
#/*Company: Teksun Microsys Pvt Ltd                                                    */
#/*Topic:                                                                              */
#/*                                                                                    */
#/*       BBAI Uart3 Pin P9.21 and P.22 testing Sample Code                            */
#/*                                                                                    */
#/*E-Mail Id: malav.patel@teksun.in                                                    */
#/**************************************************************************************/  
import serial
import time
UART3 = "/dev/ttyS2"
ser = serial.Serial(port = UART3 , baudrate=115200,timeout=0.1)
while True:
   try:
      ser.close()
      ser.open()
      ser.write('Make in India ----> working BBAI Uart 3\r\n');
      print (ser.readline())
      time.sleep(0.100)
   except:
      print ("Exception occured")
      continue
