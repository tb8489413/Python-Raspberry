import RPi.GPIO as gpio
import time
gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
pins = 12
gpio.setup(pins,gpio.OUT)

p = gpio.PWM(pins,1)
# 创建PWM实例,“1”代表频率，含义是1秒开关1次,单位Hz

p.start(0)
# 启动PWM，“0”代表占空比（DutyCycle）
# 范围 0.0 <= DutyCycle <= 100.0

try:
    while True:
        p.ChangeDutyCycle(100)
        # 改变占空比
        time.sleep(1)
        p.ChangeDutyCycle(0)
        time.sleep(1)

finally:
    p.stop()
    # 停止PWM
    gpio.cleanup()
