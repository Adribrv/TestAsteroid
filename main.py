import avatarvaisseau
from avatarvaisseau import Avatar
import core
from rocher import Rocher


def setup():
        print("Setup START---------")
        core.fps = 60
        core.WINDOW_SIZE = [800, 600]


        core.memory("avatarvaisseau",Avatar())

        core.memory("listrocher", [])
        core.memory("nbrrocher", 20)
        for c in range(0, core.memory("nbrrocher")):
            core.memory("listrocher").append(Rocher(800,800))





        print("Setup END-----------")

def run():
    core.cleanScreen()
    for creep in core.memory("listrocher"):
        creep.show(core.screen)
    core.memory("avatarvaisseau").show(core.screen)




    core.printMemory()



core.main(setup, run)




