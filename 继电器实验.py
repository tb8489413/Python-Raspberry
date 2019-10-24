import RPi.GPIO as gpio
import time
gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
pins = 20
gpio.setup(pins,gpio.OUT)

try:
    while True:
        gpio.output(pins,1)
        time.sleep(1)
        gpio.output(pins,0)
        time.sleep(1)
finally:
    gpio.cleanup()