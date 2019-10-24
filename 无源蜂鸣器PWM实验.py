import RPi.GPIO as gpio
import time
gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
pins = [20]
gpio.setup(pins[0],gpio.OUT)
# 引脚VCC接3.3V
p = gpio.PWM(pins[0],2000)
# 频率范围2kHz~5KHz
p.start(0)

try:
    while True:
        for i in range(0,101,10):
            p.ChangeDutyCycle(i)
            time.sleep(0.1)
        for i in range(100,-1,-10):
            p.ChangeDutyCycle(i)
            time.sleep(0.1)
finally:
    p.stop()
    gpio.cleanup()