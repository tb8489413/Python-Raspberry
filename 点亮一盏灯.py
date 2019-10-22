import time
import RPi.GPIO as gpio
#导入GPIO模块
gpio.setwarnings(False)
#禁用警告
gpio.setmode(gpio.BCM)
#设定GPIO引脚标号模式为BCM
gpio.setup(21,gpio.OUT)
#设定GPIO引脚21号为输出端口
gpio.output(21,True)
#21号针脚为高电平（打开）
time.sleep(3)
gpio.output(21,False)
#21号针脚为低电平（关闭）
gpio.cleanup()
#必需写入的代码（重置GPIO所有针脚为输入）
