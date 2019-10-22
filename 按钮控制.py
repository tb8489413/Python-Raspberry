import RPi.GPIO as gpio
import time
gpio.setmode(gpio.BCM)
gpio.setwarnings(False)
gpio.setup(14,gpio.OUT)
gpio.setup(16,gpio.IN,pull_up_down=gpio.PUD_UP)
gpio.setup(20,gpio.IN)
try:
    gpio.output(14,1)
    while True:
##        time.sleep(0.01)
        if (gpio.input(16)==0):
            gpio.output(14,0)
        else:
            gpio.output(14,1)
##        elif gpio.input(20)==0:
##            gpio.output(14,0)
except KeyboardInterrupt:
    pass
gpio.cleanup()
