import RPi.GPIO as gpio
import time
gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
gpio.setup(5,gpio.OUT)

try:
    while True:
        gpio.output(5,True)


finally:
    gpio.cleanup()
