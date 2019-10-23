#上拉电阻：把一个不确定的信号通过电阻连接到高电平，使该信号初始为高电平；
#下拉电阻：把一个不确定的信号通过电阻连接到低电平，使该信号初始为低电平；

import time
import RPi.GPIO as gpio
gpio.setwarnings(False)
gpio.setmode(gpio.BCM)

gpio.setup(19,gpio.IN)
# 把按钮靠近GPIO的一端用10KΩ的电阻与树莓派的GND相接
# 当按钮没有按下时GPIO口处于低电平状态，取的的值为0

gpio.setup(20,gpio.OUT)
try:
    while True:
        if gpio.input(19) == 1:
             # 此时按钮被按下的状态
            print("1")
            gpio.output(20,1)
        else:
            print("0")
            gpio.output(20, 0)
        time.sleep(0.1)
finally:
    gpio.cleanup(20)
