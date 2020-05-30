#/**************************************************************************************/
#/*File : BBAI-UART3.py                                                                */
#/*Made by: Malav Patel                                                                */
#/*Company: Teksun Microsys Pvt Ltd                                                    */
#/*Topic:                                                                              */
#/*                                                                                    */
#/*       BBAI Uart5 Pin P9.11 and P.13 testing Sample Code                            */
#/*                                                                                    */
#/*E-Mail Id: malav.patel@teksun.in                                                    */
#/**************************************************************************************/  
import serial
import time
UART5 = "/dev/ttyS4"

ser = serial.Serial(port = UART5, baudrate=115200,timeout=0.1)
while True:
   try:
      ser.close()
      ser.open()
      ser.write('Make in India ----> working BBAI Uart 5\r\n');
      print (ser.readline())
      time.sleep(0.100)
   except:
      print ("Exception occured")
      continue
