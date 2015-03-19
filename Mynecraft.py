import mcpi.minecraft as minecraft
import mcpi.block as block
import random
import time

def winner(mc):
	
	#Let Player know they won
	mc.postToChat("ZOMG YOU WON")
	
	#Get players current postion and moving them 
	cur_pos=mc.player.getTilePos()
	mc.player.setTilePos(cur_pos.x+3, cur_pos.y+3, cur_pos.z+3)


def play_game(mc):
	
	#Getting current position of player
	cur_pos=mc.player.getTilePos()
	cur_x = cur_pos.x
	cur_z = cur_pos.z

	#Randomizing where to put the Magicsquare
	new_x = random.randint(cur_x, cur_x+5)
	new_z = random.randint(cur_z, cur_z+5)

	#DEBUG LINE
	mc.postToChat("Cur x: "+ str(cur_x)+ " Cur_z: " + str(cur_z) + " new x: "+ str(new_x) + " new z: " + str(new_z))

	#Setting up flag to continue game
	won = False

	#Loop checking player position and to see if player won
	while not won:
		#Getting the players current position
		pos=mc.player.getTilePos()
		
		#DEBUG LINE
		print "x: " + str(pos.x) + " z:" + str(pos.z) 
		
		#checking if the 
		if (pos.x == new_x and pos.z == new_z):
			winner(mc)
			won=True
		time.sleep(1)

#*****Main This is where execution begins****

#Getting connection to Minecraft
mc = minecraft.Minecraft.create()

#Loop that keeps game going
while True:
	#starting the game
	play_game(mc)

	mc.postToChat("The game is afoot again")




