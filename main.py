
from grid import *
from vector import *
from world import *
import os
import time


plan =     ["#############################",
            "#    O  f f      O ~   f   ##",
            "#  f * ***     ~     f  *** #",
            "#   f**** #####        ***  #",
            "##   f    f   #   #  f  ##  #",
            "###   ****  f ##     #   f  #",
            "#   f  ****f ###  O   #     #",
            "# f ####                 f ~#",
            "#   ##   O     f   **       #",
            "#    #   **       f**  ###  #",
            "#    #   **   ~      f      #",
            "#############################"]

plan2 =   ["####################################################",
           "#              @   ####         ****             ###",
           "#   *  @  ##                 ########       OO    ##",
           "#   *    ##        O O                 ****       *#",
           "#       ##*         O O       @      ##########   *#",
           "#      ##***  *         ****                     **#",
           "#* **  #  *  ***      #########               @  **#",
           "#* **  #      *               #   *   @          **#",
           "#     ##              #   O   #  ***          ######",
           "#*            @       #       #   *        O  #    #",
           "#*       @             #  ######                 **#",
           "###          ****          ***         @         **#",
           "#       O                        @         O       #",
           "#   *     ##  ##  ##  ##               ###      *  #",
           "#   **         #              *       #####  O     #",
           "##  **  O   O  #  #    ***  ***        ###      ** #",
           "###               #   *****       @            ****#",
           "####################################################"]


world = World(plan2,{"#": Wall,"O": BouncingCritter,"*": Plant,"@": Predator})
print(world.worldToString())
while len(world.critters)>0:
    os.system("cls")
    world.turn()
    print(world.worldToString())
    print({'"#": Wall,"x": BouncingCritter,"~": WallFollower,"*": Plant, "O": Predator'})
    time.sleep(.1)

