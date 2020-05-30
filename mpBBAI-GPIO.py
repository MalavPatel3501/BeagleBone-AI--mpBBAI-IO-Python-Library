#**************************************************************************************/
#/*File : mpBBAI-GPIO.py                                                               */
#/*Made by: Malav Patel                                                                */
#/*Company: Teksun Microsys Pvt Ltd                                                    */
#/*Topic:                                                                              */
#/*                                                                                    */
#/*       BBAI GPIO Configure as a Input and Output                                    */
#/*       Read GPIO and Set GPIO direction                                             */
#/*E-Mail Id: malav.patel@teksun.in                                                    */
#/**************************************************************************************/  


from  mpBBAIIO import*
import time


GPIO = mpBBAIGpio()

IN_PIN1 = "P8_12" 
IN_PIN2 = "P8_13"

OUT_PIN1 = "P9_15"
OUT_PIN2 = "P9_25"

GPIO.setup(IN_PIN1, GPIO.INPUT)
GPIO.setup(IN_PIN2, GPIO.INPUT)

GPIO.setup(OUT_PIN1, GPIO.OUTPUT)
GPIO.setup(OUT_PIN2, GPIO.OUTPUT)


while True:
   # GPIO Input 
   PIN1_Status = GPIO.input(IN_PIN1)
   PIN2_Status = GPIO.input(IN_PIN2)
   print ("mpBBAIO Input GPIO -----> PIN1_Status  :  ",PIN1_Status, "  PIN2_Status  :   ",PIN2_Status)

   # GPIO Output
   GPIO.output(OUT_PIN1,1)
   GPIO.output(OUT_PIN2,0)
   time.sleep(1)
   GPIO.output(OUT_PIN1,0)
   GPIO.output(OUT_PIN2,1)
   time.sleep(1)
   
