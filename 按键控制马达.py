import RPi.GPIO as gpio
import turtle
import time
gpio.setwarnings(False)
##t = turtle
##turtle.shape("turtle")
##t.turtlesize(2,2,2)
def up():
    t.forward(50)
def down():
    t.backward(50)
def left():
    t.left(90)
def right():
    t.right(90)
    
def init():
    gpio.setmode(gpio.BCM)
    gpio.setup(17,gpio.OUT)#设置GPIO17（IN1）为输出
    gpio.setup(22,gpio.OUT)#设置GPIO22（IN2）为输出
    gpio.setup(23,gpio.OUT)#设置GPIO23（IN3）为输出
    gpio.setup(24,gpio.OUT)#设置GPIO24（IN4）为输出

    gpio.setup(13,gpio.OUT)#设置ENA为输出
    gpio.setup(18,gpio.OUT)#设置ENB为输出
    
def fd(t):
    '''小车前进'''
    init()
    gpio.output(13,1)#设置ENA输出为1
    gpio.output(18,1)#设置ENB输出为1
    gpio.output(17,True)#设置IN1为1
    gpio.output(22,False)#设置IN2为0
    gpio.output(23,True)#设置IN3为1
    gpio.output(24,False)#设置IN4为0
    time.sleep(t)



def bd(t):
    '''小车后退'''
    init()
    gpio.output(13,1)#设置ENA输出为1
    gpio.output(18,1)#设置ENB输出为1
    gpio.output(17,False)#设置IN1为0
    gpio.output(22,True)#设置IN2为1
    gpio.output(23,False)#设置IN3为0
    gpio.output(24,True)#设置IN4为1
    time.sleep(t)

    

def rt(t):
    '''小车右转'''
    init()
    gpio.output(13,1)#设置ENA输出为1
    gpio.output(18,1)#设置ENB输出为1
    gpio.output(17,False)#设置IN1为0
    gpio.output(22,True)#设置IN2为1
    gpio.output(23,True)#设置IN3为1
    gpio.output(24,False)#设置IN4为0
    time.sleep(t)

    

def lt(t):
    '''小车左转'''
    init()
    gpio.output(13,1)#设置ENA输出为1
    gpio.output(18,1)#设置ENB输出为1
    gpio.output(17,True)#设置IN1为1
    gpio.output(22,False)#设置IN2为0
    gpio.output(23,False)#设置IN3为0
    gpio.output(24,True)#设置IN4为1
    time.sleep(t)

try:
    while True:
        i = input("请输入动作选项：w:前进s:后退a:左转d:右转")
        if i == "w":
##            up()
            fd(0.5)
        if i == "a":
##            left()
            lt(0.5)
        if i == "s":
##            down()
            bd(0.5)
        if i == "d":
##            right()
            rt(0.5)
            gpio.output(13,0)#设置ENA输出为0
            gpio.output(18,0)#设置ENB输出为0
        else:
            gpio.output(13,0)#设置ENA输出为0
            gpio.output(18,0)#设置ENB输出为0
            
finally:
    gpio.cleanup()
    
    
    
