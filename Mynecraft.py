import mcpi.minecraft as minecraft
import mcpi.block as block
import random
import time

def winner(mc):
	mc.postToChat("ZOMG YOU WON")
	cur_pos=mc.player.getTilePos()
	mc.player.setTilePos(cur_pos.x+3, cur_pos.y+3, cur_pos.z+3)


def play_game(mc):

	cur_pos=mc.player.getTilePos()
	
	cur_x = cur_pos.x
	cur_z = cur_pos.z
	new_x = random.randint(cur_x, cur_x+5)
	new_z = random.randint(cur_z, cur_z+5)

	#DEBUG LINE DELETE AT FINAL
	mc.postToChat("Cur x: "+ str(cur_x)+ " Cur_z: " + str(cur_z) + " new x: "+ str(new_x) + " new z: " + str(new_z))

	while 1:
		pos=mc.player.getTilePos()
		print "x: " + str(pos.x) + " z:" + str(pos.z) 
		if (pos.x == new_x and pos.z == new_z):
			winner(mc)
		time.sleep(1)

####Main
mc = minecraft.Minecraft.create()
play_game(mc)




