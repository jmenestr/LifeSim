
from grid import *
from vector import *
from world import *


plan = ["############################",
            "#      #    #      o      ##",
            "#                          #",
            "#          #####           #",
            "##         #   #    ##     #",
            "###           ##     #     #",
            "#           ###      #     #",
            "#   ####                   #",
            "#   ##       o             #",
            "# o  #         o       ### #",
            "#    #                     #",
            "############################"]


world = World(plan,{"#": Wall,"o": BouncingCritter})

print(world.worldToString())

world.turn()

print(world.worldToString())