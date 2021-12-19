# LED breath

from machine import Pin, PWM
import time

def run():
    led = PWM(Pin(25))
    led.freq(1000)

    percent = 0
    step = 1
    step_now = step

    while True:
        if percent >= 100:
            percent = 100
            step_now = -step
        elif percent <= 0:
            precent = 0
            step_now = step

        led.duty_u16(int(percent/100.0*65535))
        time.sleep_ms(int(1000/(100/step)))
        percent += step_now
