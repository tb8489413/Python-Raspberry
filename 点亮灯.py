import RPi.GPIO
import time
RPi.GPIO.setmode(RPi.GPIO.BCM)
RPi.GPIO.setup(14,RPi.GPIO.OUT)
time.sleep(5)
RPi.GPIO.output(14,True)
time.sleep(10)
RPi.GPIO.output(14,False)
RPi.GPIO.cleanup()

