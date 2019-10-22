import RPi.GPIO as gpio
import time
r,g = 5,6
gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
gpio.setup(r,gpio.OUT)
gpio.setup(g,gpio.OUT)
pwm_r = gpio.PWM(r,80)
pwm_g = gpio.PWM(g,80)

pwm_r.start(0)
pwm_g.start(0)

def red():
    pwm_r.ChangeDutyCycle(0)
    pwm_g.ChangeDutyCycle(100)
    time.sleep(1)

def green():
    pwm_r.ChangeDutyCycle(100)
    pwm_g.ChangeDutyCycle(0)
    time.sleep(1)


def r_g():
    pwm_r.ChangeDutyCycle(100)
    pwm_g.ChangeDutyCycle(100)
    time.sleep(1)

try:
    while True:
        red()
        green()
        r_g()
finally:
    gpio.cleanup()
