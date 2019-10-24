import RPi.GPIO as gpio
import time
gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
pins = [20]
gpio.setup(pins[0],gpio.OUT)
# 引脚VCC接3.3V

try:
    while True:
        gpio.output(pins[0],1)
        time.sleep(1)
        gpio.output(pins[0],0)
        time.sleep(1)
finally:
    gpio.cleanup()