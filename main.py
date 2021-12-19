from machine import Pin, I2C

# # LED
# import led_breath
# import _thread

# OLED
from ssd1306 import SSD1306_I2C
import framebuf

# DHT
from dht import DHT22

import time

# Pins
LED_PIN = 25
OLED_SCL_PIN = 19
OLED_SDA_PIN = 18
DHT_PIN = 0

# OLED screen size
WIDTH  = 128
HEIGHT = 64

# # LED init
# _thread.start_new_thread(led_breath.run, ())

# Turn on LED
led = Pin(LED_PIN, Pin.OUT)
led.high()

def led_blink(times=2):
    for i in range(times):
        led.high()
        time.sleep_ms(250)
        led.low()
        time.sleep_ms(250)

# OLED init
i2c = I2C(1, scl=Pin(OLED_SCL_PIN), sda=Pin(OLED_SDA_PIN), freq=400_000)
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)

# DHT init
dht_sensor=DHT22(Pin(DHT_PIN, Pin.IN, Pin.PULL_UP), dht11=True)

while True:
    try:
        temp, humi = dht_sensor.read()
        if temp == None or humi == None:
            print('DHT failed!')
            led_blink()
            oled.text('DHT failed!', 0, 0)
            oled.show()
        else:
            led.high()
    #         print('temp:%d'%temp)
    #         print('humi:%d'%humi)
            oled.fill(0)
            oled.text('temp:%d'%temp, 8*3, 8*3)
            oled.text('humi:%d'%humi, 8*3, 8*4)
            oled.show()
    except Exception as e:
        print(e)
        led_blink()
            
    # DHT needs to sleep > 2s
    time.sleep(3)
