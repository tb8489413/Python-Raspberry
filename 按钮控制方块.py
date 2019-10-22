import RPi.GPIO as gpio
import time
import mcpi_new.minecraft as minecraft
import mcpi_new.block as block
import mcpi_new.minecraftstuff as minecraftstuff
mc = minecraft.Minecraft.create()
mcdrawing = minecraftstuff.MinecraftDrawing(mc)

gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
gpio.setup(12,gpio.IN,pull_up_down=gpio.PUD_DOWN)
# 设定12引脚号为输入
try:
    while True:
        pos = mc.player.getTilePos()
        if gpio.input(12) == 1:
            mc.setBlocks(pos.x+4,pos.y,pos.z,pos.x+4,pos.y-100,pos.z+3,0)
        else:
            gpio.input(12) == 0
finally:
    gpio.cleanup()