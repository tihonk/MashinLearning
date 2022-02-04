from threading import Thread

import numpy as np
from numpy import *
from matplotlib import pyplot

from hormones.serotonin import Serotonin


def kissOrKick():
    action = input("Press \"1\" to kiss,  press \"0\" to kick me \n")
    if(action == "1"):
        print("Thanks for your kiss!")
        Serotonin.levelUp(1)
        kissOrKick()
    elif(action == "0"):
        print("Is this what I deserve?")
        Serotonin.levelDown(1)
        kissOrKick()
    else:
        print("Illegal action! The system is broken! Restart the system.")
        return


if __name__ == '__main__':
    # for x in range(1000):
    thread = Thread(target=Serotonin.selfControl, args=(0.001,))
    thread.start()
    # Serotonin.levelUp(1)
    kissOrKick()

