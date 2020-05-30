#/**************************************************************************************/
#/* """Beagle Bone AI Python library """                                               */
#/*File : mpBBAIIO.py                                                                  */
#/*Made by: Malav Patel                                                                */
#/*Company: Teksun Microsys Pvt Ltd                                                    */
#/*Topic:                                                                              */
#/*      mapping Pin Number with Gpio number                                           */
#/*      Pin Mode setup function                                                       */
#/*	 Pin Mode output function                                                      */
#/*	 Pin Mode input function                                                       */
#/*      Configure pin functionality according to your requirement                     */
#/*E-Mail Id: malav.patel@teksun.in                                                    */ 
#/**************************************************************************************/  
import os

digitalPinDef = {
                        "P8_03":		24,
			"P8_04":		25,
			"P8_05":		192,
			"P8_06":		194,
			"P8_07":		165,
			"P8_08":		166,
			"P8_09":		178,
			"P8_10":	    164,
			"P8_11":	    75,
			"P8_12":	    74,
			"P8_13":	    107,
			"P8_14":	    109,
			"P8_15":	    99,
			"P8_16":	    125,
			"P8_17":	    242,
			"P8_18":	    105,
			"P8_19":	    106,
			"P8.20":	    190,
			"P8_21":	    189,
			"P8_22":	    23,
			"P8_23":	    22,
			"P8_24":	    192,
			"P8_25":	    191,
			"P8_26":	    124,
			"P8_27":	    119,
			"P8_28":	    115,
			"P8_29":	    118,
			"P8_30":	    116,
			"P8_31":	    238,
			"P8_32":	    239,
			"P8_33":	    237,
			"P8_34":	    235,
			"P8_35":	    236,
			"P8_36":	    234,
			"P8_37":	    232,
			"P8_38":	    233,
			"P8_39":	    230,
			"P8_40":	    231,
			"P8_41":	    228,
			"P8_42":	    229,
			"P8_43":	    226,
			"P8_44":	    227,
			"P8_45":	    224,
			"P8_46":	    225,
			"P9_11":	    241,
			"P9_12":	    128,
			"P9_13":	    172,
			"P9_14":	    121,
			"P9_15":	    76,
			"P9_16":	    122,
			"P9_17":	    209,
			"P9_18":	    208,
			"P9_19":	    195,
			"P9_20":	    196,
			"P9_21":	    67,
			"P9_22":	    179,
			"P9_23":	    203,
			"P9_24":	    175,
			"P9_25":	    177,
			"P9_26":	    174,
			"P9_27":	    111,
			"P9_28":	    113,
			"P9_29":	    139,
			"P9_30":	    140,
			"P9_31":	    138,
			"P9_41":	    180,
			"P9_42":	    114}

analogPinDef = {
            "P9_33":        "in_voltage7_raw",    #AIN4
            "P9_35":        "in_voltage4_raw",    #AIN6
            "P9_36":        "in_voltage6_raw",    #AIN5
            "P9_37":        "in_voltage3_raw",    #AIN2
            "P9_38":        "in_voltage2_raw",    #AIN3
            "P9_39":        "in_voltage0_raw",    #AIN0
            "P9_40":        "in_voltage1_raw"}    #AIN1


class mpBBAIGpio:
    gpio_directory = '/sys/class/gpio'
    HIGH = 1
    LOW = 0
    OUTPUT    = "out"
    INPUT     = "in"

    def setup(self, pin, direction):
        pinDirectory = "%s/gpio%d" % (self.gpio_directory, digitalPinDef[pin])
        if not os.path.isdir(pinDirectory):
            export_file = open("%s/export" % self.gpio_directory, 'w')
            export_file.write(str(digitalPinDef[pin]))
            export_file.close()
        temp_name = "%s/direction" % (pinDirectory)
        temp_file = open(temp_name, 'w')
        temp_file.write(direction)
        temp_file.close()

    def output(self, pin, value):
        pinDirectory = "%s/gpio%d" % (self.gpio_directory, digitalPinDef[pin])
        temp_name = "%s/value" % (pinDirectory)
        temp_file = open(temp_name, 'w')
        temp_file.write(str(value))
        temp_file.close()

    def input(self, pin):
        pinDirectory = "%s/gpio%d" % (self.gpio_directory, digitalPinDef[pin])
        temp_name = "%s/value" % (pinDirectory)
        temp_file = open(temp_name, 'r')
        inData = temp_file.read()
        temp_file.close()
        if inData == "0\n": # a 0 means it's low
                        return 0
        if inData == "1\n": # a 1 means it's high
                        return 1
        
    def analogRead(self,pin): 
        if pin in analogPinDef:            
                fileName = "/sys/bus/iio/devices/iio:device0/" + (analogPinDef [pin]) 
                fw = file(fileName, "r")
                ADCdata = fw.read()
                fw.close()
                return ADCdata
        else:
                print "analogRead error: Pin " + channel + " is not defined as an analog in pin in the pin definition."
                return -1;



