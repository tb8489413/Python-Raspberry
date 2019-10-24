
import RPi.GPIO as gpio
import time
gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
pins = [20,21,22]
gpio.setup(pins,gpio.OUT)

r = gpio.PWM(pins[0],70)
g = gpio.PWM(pins[1],70)
b = gpio.PWM(pins[2],70)
# 设置脉冲宽度调制（PWM），单位Hz

r.start(0)
g.start(0)
b.start(0)
# "开启"的时间与常规时间的时间比例

try:
    while True:
        r.ChangeDutyCycle(0)
        g.ChangeDutyCycle(100)
        b.ChangeDutyCycle(100)
        # 红色
        time.sleep(1)

        r.ChangeDutyCycle(100)
        g.ChangeDutyCycle(0)
        b.ChangeDutyCycle(100)
        # 绿色
        time.sleep(1)

        r.ChangeDutyCycle(100)
        g.ChangeDutyCycle(100)
        b.ChangeDutyCycle(0)
        # 蓝色
        time.sleep(1)

        # for i in range(0,100,5):
        #     r.ChangeDutyCycle(i)
        #     g.ChangeDutyCycle(i)
        #     time.sleep(0.01)
        # for i in range(100, -1, -5):
        #     r.ChangeDutyCycle(i)
        #     g.ChangeDutyCycle(i)
        #     time.sleep(0.01)
finally:
    r.stop()
    g.stop()
    gpio.cleanup()