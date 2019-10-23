import time
import pygame.mixer
from sys import exit
import RPi.GPIO as gpio

gpio.setwarnings(False)
gpio.setmode(gpio.BCM)

chan_list = [19,20,21]
gpio.setup(chan_list,gpio.IN,pull_up_down=gpio.PUD_DOWN)

pygame.mixer.init(48000,-16,1,1024)
# 初始化Pygame的混音器
soundA = pygame.mixer.Sound("/usr/share/sounds/alsa/Front_Center.wav")
soundB = pygame.mixer.Sound("/usr/share/sounds/alsa/Front_Left.wav")
soundC = pygame.mixer.Sound("/usr/share/sounds/alsa/Front_Right.wav")
# 加载声音文件

soundChannelA = pygame.mixer.Channel(1)
soundChannelB = pygame.mixer.Channel(2)
soundChannelC = pygame.mixer.Channel(3)
# 设置3通道

print("发音板初始化完毕")

while True:
    try:
        if gpio.input(19) == 1:
            soundChannelA.play(soundA)
        if gpio.input(20) == 1:
            soundChannelB.play(soundB)
        if gpio.input(21) == 1:
            soundChannelC.play(soundC)

        time.sleep(0.1)
    except KeyboardInterrupt:
        exit()