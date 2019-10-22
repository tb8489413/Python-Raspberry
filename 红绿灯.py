import RPi.GPIO
import time
RPi.GPIO.setmode(RPi.GPIO.BCM)
RPi.GPIO.setwarnings(False)
r = 14
y = 15
g = 18
RPi.GPIO.setup(r,RPi.GPIO.OUT)
RPi.GPIO.setup(y,RPi.GPIO.OUT)
RPi.GPIO.setup(g,RPi.GPIO.OUT)
time.sleep(3)
for i in range(3):
    RPi.GPIO.output(r,1)
    time.sleep(4)
    RPi.GPIO.output(r,0)
    RPi.GPIO.output(y,1)
    time.sleep(2)
    RPi.GPIO.output(y,0)
    RPi.GPIO.output(g,1)
    time.sleep(4)
    RPi.GPIO.output(g,0)
RPi.GPIO.cleanup()

