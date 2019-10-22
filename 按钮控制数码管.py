import RPi.GPIO as gpio
import time
gpio.setmode(gpio.BCM)
gpio.setwarnings(False)
led_port=[2,3,4,5,6,7,8]
led_9 = [2,3,4,5,7,8]
led_8 = [2,3,4,5,6,7,8]
led_7 = [4,5,8]
led_6 = [2,3,4,6,7,8]
led_5 = [4,3,2,8,7]
led_4 = [3,2,5,8]
led_3 = [4,5,2,8,7]
led_2 = [4,5,2,6,7]
led_1 = [5,8]
led_0 = [3,4,5,6,7,8]
time.sleep(3)
gpio.setup(10,gpio.IN,pull_up_down=GPIO.PUD_DOWN)
for i in led_port:
    gpio.setup(i,gpio.OUT)
def num_9():
    for i in led_9:
        gpio.output(i,True)
def num_8():
    for i in led_8:
        gpio.output(i,True)
def num_7():
    for i in led_7:
        gpio.output(i,True)
def num_6():
    for i in led_6:
        gpio.output(i,True)
def num_5():
    for i in led_5:
        gpio.output(i,True)
def num_4():
    for i in led_4:
        gpio.output(i,True)
def num_3():
    for i in led_3:
        gpio.output(i,True)
def num_2():
    for i in led_2:
        gpio.output(i,True)
def num_1():
    for i in led_1:
        gpio.output(i,True)
def num_0():
    for i in led_0:
        gpio.output(i,True)
def off():
    for i in led_port:
        gpio.output(i,False)
try:
    while True:
        if gpio.input(10)==1:
            num_9()
            time.sleep(1)
            off()
            num_8()
            time.sleep(1)
            off()
            num_7()
            time.sleep(1)
            off()
            num_6()
            time.sleep(1)
            off()
            num_5()
            time.sleep(1)
            off()
            num_4()
            time.sleep(1)
            off()
            num_3()
            time.sleep(1)
            off()
            num_2()
            time.sleep(1)
            off()
            num_1()
            time.sleep(1)
            off()
            num_0()
            time.sleep(1)
            off()
        else:
            off()
finally:
    gpio.cleanup()
