import RPi.GPIO as gpio
import time
gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
list_1 = [19,20,21,22,23,24]
n1 = 0.3
n2 = 0.2
n3 = 0.1
n4 = 0.05
n5 = 0.03
n6 = 0.01
n7 = 0.3
def set():
    for i in list_1:
        gpio.setup(i,gpio.OUT)
def open_1():
    for j in list_1:
        gpio.output(j,True)
        time.sleep(n1)
        gpio.output(j,False)
        time.sleep(n1)

def open_2():
    for j in list_1:
        gpio.output(j,True)
        time.sleep(n2)
        gpio.output(j,False)
        time.sleep(n2)

def open_3():
    for j in list_1:
        gpio.output(j,True)
        time.sleep(n3)
        gpio.output(j,False)
        time.sleep(n3)

def open_4():
    for j in list_1:
        gpio.output(j,True)
        time.sleep(n4)
        gpio.output(j,False)
        time.sleep(n4)

def open_5():
    for j in list_1:
        gpio.output(j,True)
        time.sleep(n5)
        gpio.output(j,False)
        time.sleep(n5)

def open_6():
    for j in list_1:
        gpio.output(j,True)
        time.sleep(n6)
        gpio.output(j,False)
        time.sleep(n6)
        
def open_7():
    for j in list_1:
        gpio.output(j,True)    
    time.sleep(n7)
    for j in list_1:
        gpio.output(j,False)
    time.sleep(n7)

set()
try:
    while True:
        open_1()
        open_2()
        open_3()
        for i in range(2):
            open_4()
        for i in range(4):
            open_5()
        for i in range(6):
            open_6()
        for i in range(3):
            open_7()
finally:
    print("close")
    gpio.cleanup()
    
