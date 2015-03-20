#Bringing in other packages
import mcpi.minecraft as minecraft

#Open a connection to minecraft
mc = minecraft.Minecraft.create()

#Say Hello
mc.postToChat("Hello Minecraft World")
