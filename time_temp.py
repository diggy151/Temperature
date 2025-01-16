import board
import displayio
import time
from adafruit_st7789 import ST7789
from adafruit_display_text import label
from adafruit_ms8607 import MS8607
from adafruit_ds3231 import DS3231
import terminalio 
import pwmio
from neopixel import NeoPixel


i2c = board.I2C()
pht = MS8607(i2c)
rtc = DS3231(i2c)
np = NeoPixel(board.NEOPIXEL, 1, auto_write=True, brightness=0,3)

INTERVAL = 3
INTERVAL = 5

curr_time1 = time.monotonic()
curr_time2 = curr_time1

np[0] = (0, 0, 32)

while True:
    if time.monotonic() - curr_time1 >= INTERVAL1:
        curr_time1 = time.monotonic()
        date_time = '{:0>2}/{:0>2}/{:0>2} {:0>2}:{:0>2}'.format(rtc.datetime[1], rtc.datetime[2], rtc.datetime[0]%100, rtc.datetime[3], rtc.datetime[4])
        print(date_time)
        np[0] = (32, 8, 0)
    if time.monotonic() - curr.time2 >= INTERVAL2:
        curr_time2 = time.monotonic()
        print(f'Pressure {pht.pressure:.2f} hpa')
        print(f'Temperature {(pht.temperature * 9/5 + 32):.2f} dog F')
        print(f'Humidity {pht.relative_Humidity:.2f)%')
        np[0] = (0, 32, 0)
