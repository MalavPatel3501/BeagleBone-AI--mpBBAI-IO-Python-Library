#/**************************************************************************************/
#/*File : mpBBAI-I2C.py                                                                */
#/*Made by: Malav Patel                                                                */
#/*Company: Teksun Microsys Pvt Ltd                                                    */
#/*Topic:                                                                              */
#/*                                                                                    */
#/*       BBAI I2C-5 sample code                                                       */
#/*         DAC IC AD5696                                                              */
#/*                                                                                    */
#/*E-Mail Id: malav.patel@teksun.in                                                    */
#/**************************************************************************************/  

from smbus import SMBus
import time



MaxValueDac = 65535;
MinValueDac = 0;

WRITEDAC_ABCD = 0x3F;
WRITEDAC_A = 0x31;
WRITEDAC_B = 0x32;
WRITEDAC_C = 0x34;
WRITEDAC_D = 0x38;

RefSetupReg = 0x70;

# Default I2C address:
DEFAULT_ADDRESS  = 0x0c;
I2C5 = 4

bus = SMBus(I2C5)
print bus

bus.write_i2c_block_data(DEFAULT_ADDRESS,RefSetupReg,[0,0])
bus.write_i2c_block_data(DEFAULT_ADDRESS ,WRITEDAC_ABCD,[0,0])



def set_voltage(ValueDAC,SelectedChannel):
    if ValueDAC > MaxValueDac:
       ValueDAC = MaxValueDac;
    if ValueDAC < MinValueDac:
       ValueDAC = MinValueDac;

    Data = [(ValueDAC >> 8) & 0xFF, (ValueDAC) & 0xFF]

    if SelectedChannel == 1 :
       bus.write_i2c_block_data(DEFAULT_ADDRESS,WRITEDAC_A, Data);

    elif SelectedChannel == 2 :
       bus.write_i2c_block_data(DEFAULT_ADDRESS,WRITEDAC_B, Data);

    elif SelectedChannel == 3 :
       bus.write_i2c_block_data(DEFAULT_ADDRESS,WRITEDAC_C, Data);

    elif SelectedChannel == 4 :
       bus.write_i2c_block_data(DEFAULT_ADDRESS,WRITEDAC_D, Data);

    elif SelectedChannel == 0 :
       bus.write_i2c_block_data(DEFAULT_ADDRESS,WRITEDAC_ABCD, Data);

    else :
       raise ValueError;

cnt = 0
while 1:

      cnt += 1000
      if cnt > 65000:
         cnt = 0 
      set_voltage(cnt,0)
      time.sleep(2)
