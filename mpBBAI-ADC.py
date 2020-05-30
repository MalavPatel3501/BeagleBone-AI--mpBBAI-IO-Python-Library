#/**************************************************************************************/
#/*File : mpBBAI-GPIO.py                                                               */
#/*Made by: Malav Patel                                                                */
#/*Company: Teksun Microsys Pvt Ltd                                                    */
#/*Topic:                                                                              */
#/*                                                                                    */
#/*       BBAI ADC Pin Read Sample Code                                                */
#/*                                                                                    */
#/*E-Mail Id: malav.patel@teksun.in                                                    */
#/**************************************************************************************/  

from  mpBBAIIO import*
import time

GPIO = mpBBAIGpio()

ADC_1 = "P9_33"
ADC_2 = "P9_35"

while True:
    ADC_1_Data = GPIO.analogRead(ADC_1);
    ADC_2_Data = GPIO.analogRead(ADC_2);

    print ("mpBBAI ADC Pin Read ------> ADC_1_Data  :  ",ADC_1_Data,"  ADC_2_Data  :  ",ADC_2_Data );
    time.sleep(1)
