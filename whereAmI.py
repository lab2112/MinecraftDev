import mcpi.minecraft as minecraft
import time

#Getting Connection to Minecraft
mc=minecraft.Minecraft.create()

while True:
	time.sleep(1)

	#Getting Player position
	pos = mc.player.getTilePos()

	#Posting player position
	mc.postToChat("x="+str(pos.x) + " y="+str(pos.y) + " z="+str(pos.z))