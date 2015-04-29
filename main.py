
from grid import *
from vector import *
from world import *
import os
import time


plan =     ["#############################",
            "#  *                       ##",
            "#                           #",
            "#          #####            #",
            "##          #   #    ##     #",
            "###           ##     #      #",
            "#           ###      #      #",
            "#   ####                    #",
            "#   ##          *           #",
            "#    #                 ###  #",
            "#    #           ~          #",
            "#############################"]


world = World(plan,{"#": Wall,"f": BouncingCritter,"x": BouncingCritter,"~": WallFollower,"*": Plant})

for i in range(100):
    world.turn()
    print(world.worldToString())
    if world.isempty():
        print("All critters have died.")
        break
    time.sleep(.1)


