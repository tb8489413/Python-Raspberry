import RPi.GPIO as gpio
import time
gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
gpio.setup(17,gpio.OUT)#设置GPIO17（IN1）为输出
gpio.setup(22,gpio.OUT)#设置GPIO22（IN2）为输出
gpio.setup(23,gpio.OUT)#设置GPIO23（IN3）为输出
gpio.setup(24,gpio.OUT)#设置GPIO24（IN4）为输出

gpio.setup(13,gpio.OUT)#设置ENA为输出
gpio.setup(18,gpio.OUT)#设置ENB为输出

p1 = gpio.PWM(13,1000)#设置1000HZ的PWM于13针脚
p1.start(15)#以占空比15启动PWM脉冲
input("15")
p1.ChangeDutyCycle(25)#改变占空比为25
input("25")
p1.ChangeDutyCycle(80)#改变占空比为80
input("80")
p1.ChangeDutyCycle(100)#改变占空比为100
input("100")
p1.stop()
gpio.cleanup()


