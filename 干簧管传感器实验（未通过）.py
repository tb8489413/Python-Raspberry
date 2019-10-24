import RPi.GPIO as gpio
import time
gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
pins = [20,21,22]
gpio.setup(pins[0],gpio.IN)
# 引脚VCC接5V
gpio.setup(pins[1],gpio.OUT)
gpio.setup(pins[2],gpio.OUT)

try:
    while True:
        if gpio.input(pins[0]) == 1:
            gpio.output(pins[1],1)
            gpio.output(pins[2],0)
        if gpio.input(pins[0]) == 0:
            gpio.output(pins[2],1)
            gpio.output(pins[1],0)
finally:
    gpio.cleanup()