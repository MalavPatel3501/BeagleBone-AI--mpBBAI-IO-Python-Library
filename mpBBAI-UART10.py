#/**************************************************************************************/
#/*File : BBAI-UART3.py                                                                */
#/*Made by: Malav Patel                                                                */
#/*Company: Teksun Microsys Pvt Ltd                                                    */
#/*Topic:                                                                              */
#/*                                                                                    */
#/*       BBAI Uart10 Pin P9.24 and P.26 testing Sample Code                            */
#/*                                                                                    */
#/*E-Mail Id: malav.patel@teksun.in                                                    */
#/**************************************************************************************/  
import serial
import time
UART10 = "/dev/ttyS1"

ser = serial.Serial(port = UART10, baudrate=115200,timeout=0.1)
while True:
   try:
      ser.close()
      ser.open()
      ser.write('Make in India ----> working BBAI Uart 10\r\n');
      print (ser.readline())
      time.sleep(0.100)
   except:
      print ("Exception occured")
      continue
