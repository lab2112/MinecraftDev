import mcpi.minecraft as minecraft
import mcpi.block as block
import random

mc = minecraft.Minecraft.create()

cur_pos=mc.player.getTilePos()

play_game(cur_pos)

def play_game(cur_pos):
    cur_x = cur_pos.x
    cur_z = cur_pos.z
    new_x = random.randomint(cur_x, cur_x+5)
    new_y = random.randomint(cur_y, cur_y+5)
    
