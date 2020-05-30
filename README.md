# BeagleBone-AI--mpBBAI-IO-Python-Library
Update pin functionality and python Library of BeagleBone AI (am5729-beagleboneai) board

/**************************************************************************************/
/*File : README.md                                                                    */
/*Made by: Malav Patel                                                                */
/*Company: Teksun Microsys Pvt Ltd                                                    */
/*Topic:                                                                              */
/*      explain Process of Pin Muxing for Beagle Bone AI Board                        */
/*      Make .dts file and update environment file                                    */
/*      Configure pin functionality according to your requirement                     */
/*E-Mail Id: malav.patel@teksun.in                                                    */
/**************************************************************************************/  


PINMUXING

Pinmux Procedure
If you need to configure the pins as inputs, outputs, I2C, UART and PWM in Beagle Bone AI.
This is a process called Pinmuxing (pin multiplexing).  Here is a procedure for setting your 
pinmux configuration to the one that was used for my board:

Command:
cd #(or wherever you want to clone the next line to)  
git clone https://github.com/beagleboard/BeagleBoard-DeviceTrees -b v4.14.x-ti  
cd BeagleBoard-DeviceTrees
nano src/arm/am5729-beagleboneai.dts #(defuault dts file below)  

PINMODE Refrence Link and follow section 7. Connectors of BeagleBone AI System Reference Manual:
https://github.com/beagleboard/beaglebone-ai/wiki/System-Reference-Manual
Also My updated am5729-beagleboneai.dts file in this folder so you can easily understand.

Note: MODE0 means (pinnumber)a
      MODE2 mean  (pinnumber)b

example purpose i use P8.45 and P8.46 Pin:

	         P8.45	       P8.46

GPIO        224            225

BALL        F11            G10

REG         0x15DC          0x15E0

MODE 0      vout1_d0        vout1_d1

1

2           uart5_rxd       uart5_txd

3           vin4a_d16       vin4a_d17

4           vin3a_d16       vin3a_d17

5

6

7

8           spi3_cs2

9

10          pr1_uart0_cts_n     pr1_uart0_rts_n

11

12          pr2_pru1_gpi18      pr2_pru1_gpi19

13          pr2_pru1_gpo18      pr2_pru1_gpo19

14          gpio8_0             gpio8_1

15          Driver off          Driver off

2nd BALL    B7                  A10

2nd REG     0x161C              0x1638

2nd MODE 0  vout1_d16           vout1_d23

2nd 1

2nd 2       uart7_rxd           emu19

2nd 3       vin4a_d0            vin4a_d7

2nd 4       vin3a_d0            vin3a_d7

2nd 5

2nd 6

2nd 7

2nd 8                           spi3_cs3

2nd 9

2nd 10      pr2_edio_data_in0       pr2_edio_data_in7

2nd 11      pr2_edio_data_out0      pr2_edio_data_out7

2nd 12      pr2_pru0_gpi13          pr2_pru0_gpi20

2nd 13      pr2_pru0_gpo13          pr2_pru0_gpo20

2nd 14      gpio8_16                gpio8_23

2nd 15      Driver off              Driver off


1)  GPIO Output Configuration Method:
    update GPIO pin configuration accroding to your requirement
      cape_pins_default: cape_pins_default {
        #example   PINREG define in Header8&9 Pin Number and REG file
        #0x379C P8.3:
        #DRA7XX_CORE_IOPAD(0x379C, MUX_MODE14)                         //if you need  defult as low
        #DRA7XX_CORE_IOPAD(0x379C, PIN_OUTPUT_PULLUP | MUX_MODE14)     //if you need defult as high
       
        DRA7XX_CORE_IOPAD(PINREG, MUX_MODE14)
      }


2)  GPIO Input Configuration Method:
    update INPUT GPIO pin configuration accroding to your requirement
      cape_pins_default: cape_pins_default {
        #example   PINREG define in Header8&9 Pin Number and REG file
        #0x350C P8.12: as a Input Pin always set Mode pr2_pru0_gpi
        DRA7XX_CORE_IOPAD(0x350C, PIN_INPUT | MUX_MODE12) /* AG6: P8.12: pr2_pru0_gpi */
        
        DRA7XX_CORE_IOPAD(PINREG, PIN_INPUT |MUX_MODE12) /*Mode check in section 7 in below link */
                                                         /* https://github.com/beagleboard/beaglebone-ai/wiki/System-Reference-Manual */
      }


3)  UART3 Configuration Method:
      cape_pins_default: cape_pins_default {....
         make comment "//" UART3 PIN in this function
         //DRA7XX_CORE_IOPAD(0x34F0, MUX_MODE14) /* AF8: P9.21a: vin1a_vsync0.off */
		 //DRA7XX_CORE_IOPAD(0x37C4, MUX_MODE14) /* B22: P9.21b: spi2_d1.off */
		 //DRA7XX_CORE_IOPAD(0x369C, MUX_MODE14) /* B26: P9.22a: xref_clk2.off */
		 //DRA7XX_CORE_IOPAD(0x37C0, MUX_MODE14) /* A26: P9.22b: spi2_sclk.off */
				
       .......}

      &uart3 {
          status = "okay";
          pinctrl-names = "default";
          pinctrl-0 = <&uart3_pins>;
        };
      &dra7_pmx_core {
          uart3_pins: uart3 {
            pinctrl-single,pins = <
                DRA7XX_CORE_IOPAD( 0x34F0, PIN_OUTPUT     | MUX_MODE15)  // P9.21a uart2_txd
                DRA7XX_CORE_IOPAD( 0x37C4, PIN_OUTPUT     | MUX_MODE1 )  // P9.21b
                DRA7XX_CORE_IOPAD( 0x369C, PIN_INPUT      | MUX_MODE15)  // P9.22a uart10_rxd
                DRA7XX_CORE_IOPAD( 0x37C0, PIN_INPUT      | MUX_MODE1 )  // P9.22b (shared pin)
          >;
        };
    };


4)  UART5 Configuration Method:
      cape_pins_default: cape_pins_default {....
         make comment "//" UART5 PIN in this function
         //DRA7XX_CORE_IOPAD(0x372C, MUX_MODE14) /* B19: P9.11a: mcasp3_axr0.off */
		 //DRA7XX_CORE_IOPAD(0x3620, MUX_MODE14) /* B8: P9.11b: vout1_d17.off */
		 //DRA7XX_CORE_IOPAD(0x3730, MUX_MODE14) /* C17: P9.13: mcasp3_axr1.off */
					
      .......}

      &uart5 {
          status = "okay";
          pinctrl-names = "default";
          pinctrl-0 = <&uart5_pins>;
        };
      &dra7_pmx_core {
          uart5_pins: uart5 {
            pinctrl-single,pins = <
                DRA7XX_CORE_IOPAD( 0x372C, PIN_INPUT    | MUX_MODE4 )  
                DRA7XX_CORE_IOPAD( 0x3620, PIN_INPUT    | MUX_MODE15)  
                DRA7XX_CORE_IOPAD( 0x3730, PIN_OUTPUT   | MUX_MODE4 )  
          
          >;
       };
     };


5)  UART10 Configuration Method:
    
    cape_pins_default: cape_pins_default {....
         make comment "//" UART10 PIN in this function
         //DRA7XX_CORE_IOPAD(0x368C, MUX_MODE14) /* F20: P9.24: gpio6_15.off */
		 //DRA7XX_CORE_IOPAD(0x3688, MUX_MODE14) /* E21: P9.26a: gpio6_14.off */
		 //DRA7XX_CORE_IOPAD(0x3544, MUX_MODE14) /* AE2: P9.26b: vin1a_d20.off */
			
     .......}

    &uart10 {
          status = "okay";
          pinctrl-names = "default";
          pinctrl-0 = <&uart10_pins>;
        };
    &dra7_pmx_core {
          uart10_pins: uart10 {
            pinctrl-single,pins = <
                DRA7XX_CORE_IOPAD( 0x368C, PIN_OUTPUT     | MUX_MODE3  )  // P9.24 uart10_txd
                DRA7XX_CORE_IOPAD( 0x3688, PIN_INPUT      | MUX_MODE3  )  // P9.26a uart10_rxd
                DRA7XX_CORE_IOPAD( 0x3544, PIN_INPUT      | MUX_MODE15 )  // P9.26b (shared pin)
          >;
        };
    };


6)  I2c5 Configuration Method:
      cape_pins_default: cape_pins_default {....
         make comment "//" UART10 PIN in this function
         //DRA7XX_CORE_IOPAD(0x37CC, MUX_MODE14) /* B24: P9.17a: spi2_cs0.off */
		 //DRA7XX_CORE_IOPAD(0x36B8, MUX_MODE14) /* F12: P9.17b: mcasp1_axr1.off */
		 //DRA7XX_CORE_IOPAD(0x37C8, MUX_MODE14) /* G17: P9.18a: spi2_d0.off */
		 //DRA7XX_CORE_IOPAD(0x36B4, MUX_MODE14) /* G12: P9.18b: mcasp1_axr0.off */				
     .......}
      
      &i2c5 {
        status = "okay";
        clock-frequency = <400000>;
        pinctrl-names = "default";
        pinctrl-0 = <&i2c5_pins>;

      };
      &dra7_pmx_core {
        i2c5_pins: i2c5 {
            pinctrl-single,pins = <
                DRA7XX_CORE_IOPAD( 0x37CC, PIN_INPUT_PULLUP | MUX_MODE15  )  // scl
                DRA7XX_CORE_IOPAD( 0x36B8, PIN_INPUT_PULLUP | MUX_MODE10 )  // (shared pin)
                DRA7XX_CORE_IOPAD( 0x37C8, PIN_INPUT_PULLUP | MUX_MODE15  )  // sda
                DRA7XX_CORE_IOPAD( 0x36B4, PIN_INPUT_PULLUP | MUX_MODE10 )  // (shared pin)
            >;
        };
      };


7)  SPI Configuration Method(Not Working right now i am working on that):
      cape_pins_default: cape_pins_default {....
         make comment "//" UART10 PIN in this function
         //DRA7XX_CORE_IOPAD(0x36D8, MUX_MODE14) /* A11: P9.29a: mcasp1_axr9.off */
		 //DRA7XX_CORE_IOPAD(0x36A8, MUX_MODE14) /* D14: P9.29b: mcasp1_fsx.off */
		 //DRA7XX_CORE_IOPAD(0x36DC, MUX_MODE14) /* B13: P9.30: mcasp1_axr10.off */
		 //DRA7XX_CORE_IOPAD(0x36D4, MUX_MODE14) /* B12: P9.31a: mcasp1_axr8.off */
		 //DRA7XX_CORE_IOPAD(0x36A4, MUX_MODE14) /* C14: P9.31b: mcasp1_aclkx.off */
			......}
       
       &mcspi3 {
        #address-cells = <1>;
        #size-cells = <0>;
        status = "okay";
        cs-gpios = <0>, <&gpio7 11 0>;
        channel@0 {
                #address-cells = <1>;
                #size-cells = <0>;
                compatible = "spidev";
                reg = <0>;
                spi-max-frequency = <24000000>;
        };
      };
  
      &dra7_pmx_core {  
        mcspi3_pins: mcspi3_pins {  
            pinctrl-single,pins = <  
                DRA7XX_CORE_IOPAD( 0x36D8, PIN_INPUT_PULLUP | MUX_MODE3  )    //P9.29a   
                DRA7XX_CORE_IOPAD( 0x36A8, PIN_INPUT_PULLUP | MUX_MODE15 )    //P9.29b
                DRA7XX_CORE_IOPAD( 0x36DC, PIN_OUTPUT_PULLUP| MUX_MODE3  )    //P9.30   
                DRA7XX_CORE_IOPAD( 0x36D4, PIN_INPUT_PULLUP | MUX_MODE3  )    //P9.31a   
                DRA7XX_CORE_IOPAD( 0x36A4, PIN_INPUT_PULLUP | MUX_MODE15 )    //P9.31b
            >;  
        };  
     };  
  Note: SPI is Not proper working i am working on that Clk is not generate issue  


8)  PWM Configuration Method:

example: P9_14   0x35AC                  
check using command sys/class/pwm/pwm-0:0/
DRA7XX_CORE_IOPAD(0x35AC, MUX_MODE10) /* D6: P9.14: PWM */

&epwmss0 {
        status = "okay";
};

&epwmss1 {
        status = "okay";
};

&epwmss2 {
        status = "okay";
};

&ehrpwm1 {
        status = "okay";
};

&ehrpwm2 {
        status = "okay";
};



9) ADC Configuration Method:

    /* STMPE811 touch screen controller */
	 stmpe811@41 {
		  compatible = "st,stmpe811";
		  reg = <0x41>;
		  interrupts = <30 IRQ_TYPE_LEVEL_LOW>;
		  interrupt-parent = <&gpio2>;
		  interrupt-controller;
		  id = <0>;
		  blocks = <0x5>;
		  irq-trigger = <0x1>;
		  st,mod-12b = <1>; /* 12-bit ADC */
		  st,ref-sel = <0>; /* internal ADC reference */
		  st,adc-freq = <1>; /* 3.25 MHz ADC clock speed */
		  st,sample-time = <4>; /* ADC converstion time: 80 clocks */

		  pinctrl-names = "default";
		  pinctrl-0 = <&adc_pins_default>;

		  stmpe_adc {
			  compatible = "st,stmpe-adc";
			  st,norequest-mask = <0x00>; /* mask any channels to be used by touchscreen */
			  adc0: iio-device@0 {
				  #io-channel-cells = <1>;
				  iio-channels = <&adc0 4>, <&adc0 1>, <&adc0 2>, <&adc0 3>, <&adc0 4>, <&adc0 5>, <&adc0 6>;
				  iio-channel-names = "AIN0_P9_39", "AIN1_P9_40", "AIN2_P9_37", "AIN3_P9_38",
					  "AIN4_P9_33", "AIN5_P9_36", "AIN6_P9_35";
			  };
		  };

		  stmpe_touchscreen {
			  status = "disabled";
			  compatible = "st,stmpe-ts";
		  };

		  stmpe_gpio {
			  compatible = "st,stmpe-gpio";
		  };

		  stmpe_pwm {
			  compatible = "st,stmpe-pwm";
			  #pwm-cells = <2>;
		  };
	  };
   };


Command:
/*not need to do again if you done before*/
//cd #(or wherever you want to clone the next line to)  
//git clone https://github.com/beagleboard/BeagleBoard-DeviceTrees -b v4.14.x-ti  
//cd BeagleBoard-DeviceTrees
//nano src/arm/am5729-beagleboneai.dts #(defuault dts file below)  

cd BeagleBoard-DeviceTrees  
nano src/arm/am5729-beagleboneai-mpcustom.dtb
//copy and paste .dts file and update pin configuration according to your requirement
make src/arm/am5729-beagleboneai-mpcustom.dtb
make install  
sudo cp src/arm/am5729-beagleboneai-custom.dtb /boot/dtbs/  
sudo nano /boot/uEnv.txt #(configure: dtb=am5729-beagleboneai-mpcustom.dtb)  
sudo reboot  

/* nano /boot/uEnv.txt          ----------FIle */
#Docs: http://elinux.org/Beagleboard:U-boot_partitioning_layout_2.0

uname_r=4.14.108-ti-r131
#uuid=
dtb=am5729-beagleboneai-mpcustom.dtb

cmdline=coherent_pool=1M net.ifnames=0 rng_core.default_quality=100 quiet

#In the event of edid real failures, uncomment this next line:
#cmdline=coherent_pool=1M net.ifnames=0 rng_core.default_quality=100 quiet video=HDMI-A-1:1024x768@60e

##enable x15: eMMC Flasher:
##make sure, these tools are installed: dosfstools rsync
#cmdline=init=/opt/scripts/tools/eMMC/init-eMMC-flasher-v3-no-eeprom.sh



