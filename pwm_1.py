import RPi.GPIO as gpio
import time
gpio.setmode(gpio.BCM)
gpio.setwarnings(False)
gpio.setup(14,gpio.OUT)
gpio.setup(15,gpio.OUT)

##p = gpio.PWM(14,80)
##p.start(90)
gpio.output(14,True)
gpio.output(15,True)
time.sleep(2)
gpio.output(14,False)
gpio.output(15,False)
##p.stop()
gpio.cleanup()
