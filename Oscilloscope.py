"""
VDD - pin-17 -3.3v
GND- GND -pin-6
SCL- pin-5-GPIO 3
SDA-pin-3 -GPIO 2

apt-get install build-essential python-dev python-smbus git

git clone https://github.com/adafruit/Adafruit_Python_ADS1x15.git
cd Adafruit_Python_ADS1x15
"""
import time 
import board 
import busio 
import adafruit_ads1x15.ads1015 as ADS 
from adafruit_ads1x15.analog_in import AnalogIn 
i2c = busio.I2C(board.SCL, board.SDA) 
ads = ADS.ADS1015(i2c)  
chan = AnalogIn(ads, ADS.P0) 
chan = AnalogIn(ads, ADS.P0, ADS.P1) 
print("{:>5}\t{:>5}".format("raw", "v"))
while True:   
   print("{:>5}\t{:>5.3f}".format(chan.value, chan. voltage))    
   time.sleep(0.5)
