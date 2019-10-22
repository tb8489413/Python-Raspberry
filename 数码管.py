import RPi.GPIO as gpio
import time
gpio.setmode(gpio.BCM)
gpio.setwarnings(False)
led_port=[2,3,4,5,6,7,8,9]
led_io=[1,1,1,1,1,1,1,1,0]
for i in led_port:
    a=gpio.setup(i,gpio.OUT)
time.sleep(3)   
for j in range(8):
    gpio.output(led_port[j],True)
    print(j)
    time.sleep(1)
    gpio.output(led_port[j],False)
    time.sleep(0.3)

input("finished?")
gpio.cleanup()
