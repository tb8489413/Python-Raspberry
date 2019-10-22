import mcpi.minecraft as minecraft
import mcpi.block as block
import RPi.GPIO as gpio
import time
mc = minecraft.Minecraft.create()
gpio.setmode(gpio.BCM)
gpio.setwarnings(False)
#禁用警告信息
gpio.setup(15,gpio.OUT)
gpio.setup(14,gpio.OUT)
gpio.setup(13,gpio.OUT)
def led_on():
    gpio.output(15,True)
    gpio.output(14,1)
    gpio.output(13,gpio.HIGH)
    
def led_off():
    gpio.output(15,False)
    gpio.output(14,0)
    gpio.output(13,gpio.LOW)
    

def mf():
    pos = mc.player.getTilePos()
    if pos.x ==5 and pos.y==4 and pos.z == -10:
        time.sleep(1)
        mc.postToChat("welcom home!")
        led_on()
    else:
        led_off()
        
try:
    while True:
        mf()


finally:
    print("开始重置gpio")
    gpio.cleanup()
    
