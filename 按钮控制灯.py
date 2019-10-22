import RPi.GPIO as gpio
import time
gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
gpio.setup(19,gpio.IN)
gpio.setup(20,gpio.OUT)
try:
    while True:
        if gpio.input(19)==0:
            gpio.output(20,False)
        if gpio.input(19)==1:
            gpio.output(20,True)
           
        
finally:
    print("close")
    gpio.cleanup()
