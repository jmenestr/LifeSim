
from grid import *
from vector import *
from world import *
import os
import time


plan = ["############################",
            "#      #    #      f      ##",
            "# f                  f     #",
            "#      x   #####           #",
            "##     f    #   #    ##  f #",
            "###           ##     #     #",
            "#           ###      #     #",
            "#   ####         x         #",
            "#   ##       f         x   #",
            "# f  #         f       ### #",
            "#    #     x            f  #",
            "############################"]


world = World(plan,{"#": Wall,"f": BouncingCritter,"x": BouncingCritter})

print(world.worldToString())

for i in range(100):
    os.system("cls")
    world.turn()
    print(world.worldToString())
    time.sleep(0.250)



