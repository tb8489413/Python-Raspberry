import RPi.GPIO as gpio
import time
import random
gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
list_1 = [5,6,7,8,9,10]
n1 = 0.1
n2 = 0.05
n3 = 0.04
n4 = 0.03
n5 = 0.02
n6 = 0.01
list_2 = [0.1,0.05,0.03,0.02,0.01,0.0025]

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
    for j in reversed(list_1):
        gpio.output(j,True)
        time.sleep(n1)
        gpio.output(j,False)
        time.sleep(n1)

def open_8():
    for j in reversed(list_1):
        gpio.output(j,True)
        time.sleep(n2)
        gpio.output(j,False)
        time.sleep(n2)
        
def open_9():
    for j in reversed(list_1):
        gpio.output(j,True)
        time.sleep(n3)
        gpio.output(j,False)
        time.sleep(n3)

def open_10():
    for j in reversed(list_1):
        gpio.output(j,True)
        time.sleep(n4)
        gpio.output(j,False)
        time.sleep(n4)

def open_11():
    for j in reversed(list_1):
        gpio.output(j,True)
        time.sleep(n5)
        gpio.output(j,False)
        time.sleep(n5)
        
def open_12():
    for j in reversed(list_1):
        gpio.output(j,True)
        time.sleep(n6)
        gpio.output(j,False)
        time.sleep(n6)

def open_all():
    for j in list_1:
        gpio.output(j,True)

def close_all():
    for k in list_1:
        gpio.output(k,False)
def open_13():
    open_all()
    for i in list_2:
        time.sleep(i)
    close_all()
    for i in list_2:
        time.sleep(i)
def open_14():
    global n7
    n7 = random.choice(list_1)
    gpio.output(n7,True)
    time.sleep(0.1)
    gpio.output(n7,False)
    time.sleep(0.1)

##def open_4():
##    for j in list_1:
##        gpio.output(j,True)
##        for i in list_2:
##            time.sleep(i)
##        gpio.output(j,False)
##        for i in list_2:
##            time.sleep(i)
set()
try:
    while True:
        open_1()
        open_2()
        open_3()
        open_4()
        open_5()
        for i in range(6):
            open_6()
        time.sleep(0.5)
        open_7()
        open_8()
        open_9()
        open_10()
        open_11()
        for i in range(6):
            open_12()
        time.sleep(0.5)
        for i in range(6):
            open_13()
        time.sleep(0.5)
        for i in range(25):
            open_14()
        
##        time.sleep(1)
    
finally:
    gpio.cleanup()
