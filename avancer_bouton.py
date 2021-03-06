import RPi.GPIO as gpio
import time
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x, y, z = mc.player.getPos()

buttonL = 18
buttonR = 15

gpio.setmode(gpio.BCM)
gpio.setup(buttonL, gpio.IN, pull_up_down=gpio.PUD_UP)
gpio.setup(buttonR, gpio.IN, pull_up_down=gpio.PUD_UP)

left0 = False
right0 = False

while True:
	left = gpio.input(buttonL)
	right = gpio.input(buttonR)

	x,y,z = mc.player.getPos()

	if not left and left0:
		mc.postToChat("pushed left")
	if left and not left0:
		mc.postToChat("released left")
		mc.player.setPos(x+5, y, z)

	left0 = left

	if not right and right0:
		mc.postToChat("pushed right")
	if right and not left0:
		mc.postToChat("realeased right")
		mc.player.setPos(x+5, y, z)
	right0 = right



