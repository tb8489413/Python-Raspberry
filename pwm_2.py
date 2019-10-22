import RPi.GPIO as gpio
import time
gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
gpio.setup(14,gpio.OUT)
p = gpio.PWM(14,50)
p.start(0)
try:
    while True:
        for i in range(0,101,5):
            p.ChangeDutyCycle(i)
            time.sleep(0.1)
        for i in range(100,-1,-5):
            p.ChangeDutyCycle(i)
            time.sleep(0.1)
except KeyboardInterrupt:
    pass
p.stop()
gpio.cleanup()
