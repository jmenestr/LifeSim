
from grid import *
from vector import *
from world import *
import os
import time


plan =     ["#############################",
            "#        x        ~   x    ##",
            "#   * ***     ~     x  **   #",
            "#    **** #####        **   #",
            "##          #   #  x  ##    #",
            "###   ****  f ##     #   x  #",
            "#     ****x ###      #      #",
            "#   ####                   ~#",
            "#   ##         x   **       #",
            "# ** #   **       x**  ###  #",
            "#    #   **   ~    xxx      #",
            "#############################"]


world = World(plan,{"#": Wall,"f": BouncingCritter,"x": BouncingCritter,"~": WallFollower,"*": Plant})
print(world.worldToString())
x = 0
while len(world.critters)>0:
    x+=1
    os.system("clear")
    world.turn()
    print(world.worldToString())
    time.sleep(.1)

print(x)