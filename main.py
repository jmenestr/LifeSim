
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
           "#   *  O  ##                 ########       OO    ##",
           "#   *    ##        O O                 ****       *#",
           "#       ##*         O O       @      ##########   *#",
           "#      ##***  *         ****                     **#",
           "#* **  #  *  ***      #########              O   **#",
           "#* **  #      *               #   *   O          **#",
           "#     ##              #   O   #  ***          ######",
           "#*            @       #       #   *        O  #    #",
           "#*       @             #  ######                 **#",
           "###          ****          ***         @         **#",
           "#       O                        O         O       #",
           "#   *     ##  ##  ##  ##               ###      *  #",
           "#   **         #              *       #####  O     #",
           "##  **  O   O  #  #    ***  ***        ###      ** #",
           "###               #   *****       O            ****#",
           "####################################################"]


world = World(plan2,{"#": Wall,"O": BouncingCritter,"*": Plant,"@": Predator})
print(world.worldToString())
x = 0
while len(world.critters)>0:
    x+=1
    os.system("clear")
    world.turn()
    print(world.worldToString())
    print({'"#": Wall,"x": BouncingCritter,"~": WallFollower,"*": Plant, "O": Predator'})
    time.sleep(.1)

print(x)