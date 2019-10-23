#上拉电阻：把一个不确定的信号通过电阻连接到高电平，使该信号初始为高电平；
#下拉电阻：把一个不确定的信号通过电阻连接到低电平，使该信号初始为低电平；

import time
import RPi.GPIO as gpio
gpio.setwarnings(False)
gpio.setmode(gpio.BCM)

gpio.setup(19,gpio.IN,pull_up_down=gpio.PUD_UP)
# 按钮连接的GPIO针脚的模式设置为信号输入模式，同时默认拉高GPIO口电平，
# 当GND没有被接通时，GPIO口处于高电平状态，取的的值为1

gpio.setup(20,gpio.OUT)
try:
    while True:
        if gpio.input(19) == 0:
            # 此时按钮被按下的状态
            print("1")
            gpio.output(20,1)
        else:
            print("0")
            gpio.output(20, 0)
        time.sleep(0.1)
finally:
    gpio.cleanup(20)
