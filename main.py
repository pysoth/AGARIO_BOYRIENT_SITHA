
import core
import pygame

def setup():
    print("setup start....")
    core.fps = 30
    core.WINDOW_SIZE = [400,400]
    core.memory("listcreep")
    core.memory("nbcreep",100)


    for i in range(0, core.memory("nbcreep")):
        core.memory("nbcreep").append(creep)

    print("setup END......")


def run () :
    core.cleanScreen()
    core.printMemory()
    for creep in core.memory("listcreep"):
        creep.show(core.screen)
