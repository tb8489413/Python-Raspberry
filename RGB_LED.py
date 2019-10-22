import RPi.GPIO as gpio
import time
r,g,b = 5,6,7
gpio.setmode(gpio.BCM)
gpio.setwarnings(False)
gpio.setup(r,gpio.OUT)
gpio.setup(g,gpio.OUT)
gpio.setup(b,gpio.OUT)

pwm_r = gpio.PWM(r,70)
pwm_g = gpio.PWM(g,70)
pwm_b = gpio.PWM(b,70)

pwm_r.start(0)
pwm_g.start(0)
pwm_b.start(0)

def red():
    gpio.output(r,True)
    time.sleep(1)
    gpio.output(r,False)

def green():
    gpio.output(g,True)
    time.sleep(1)
    gpio.output(g,False)

def blue():
    gpio.output(b,True)
    time.sleep(1)
    gpio.output(b,False)

def r_g():
    gpio.output(r,True)
    gpio.output(g,True)
    time.sleep(1)
    gpio.output(r,False)
    gpio.output(g,False)

def r_b():
    gpio.output(r,True)
    gpio.output(b,True)
    time.sleep(1)
    gpio.output(r,False)
    gpio.output(b,False)

def g_b():
    gpio.output(g,True)
    gpio.output(b,True)
    time.sleep(1)
    gpio.output(g,False)
    gpio.output(b,False)

def r_g_b():
    gpio.output(r,True)
    gpio.output(g,True)
    gpio.output(b,True)
    time.sleep(1)
    gpio.output(r,True)
    gpio.output(g,False)
    gpio.output(b,False)

def pwm_rgb():
    for r in range(0,101,20):
        pwm_r.ChangeDutyCycle(r)
        for g in range(0,101,20):
            pwm_g.ChangeDutyCycle(g)
            for b in range(0,101,20):
                pwm_b.ChangeDutyCycle(b)
                time.sleep(0.5)
            
try:    
    while True:
##        red()
##        green()
##        blue()
##        r_g()
##        r_b()
##        g_b()
##        r_g_b()
        pwm_rgb()
finally:
    gpio.cleanup()
