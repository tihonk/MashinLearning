import math
from time import sleep


MAX_SEROTONIN_LEVEL = 220.0
MIN_SEROTONIN_LEVEL = 50.0


def getFactor(serotoninLevel, isFilling = False):
    if(serotoninLevel > MAX_SEROTONIN_LEVEL):
        return 0.0
    elif(serotoninLevel < MIN_SEROTONIN_LEVEL):
        return 0.0
    elif(isFilling):
        return (-(serotoninLevel - MIN_SEROTONIN_LEVEL) / 56.667) + 3
    else:
        return ((serotoninLevel - MAX_SEROTONIN_LEVEL) / 56.667) + 3


def getSelfChangingFactor(serotoninLevel):
    # serotonin_50 = 2.006
    serotonin_100 = 1.6853
    # serotonin_135 = 1.46
    # serotonin_170 = 1.088
    maxSerotoninLevel = serotoninLevel if serotoninLevel > MAX_SEROTONIN_LEVEL else MAX_SEROTONIN_LEVEL
    changingResult = 1/6.5 * math.sqrt(-serotoninLevel + maxSerotoninLevel)
    selfChangingFactor = serotonin_100 - changingResult
    return selfChangingFactor


class Serotonin:
    serotoninLevel = 135

    def levelUp(self: float):
        serotoninLevel = Serotonin.serotoninLevel
        Serotonin.serotoninLevel = serotoninLevel + (self * getFactor(serotoninLevel, True))
        print("SEROTONIN level changed to up on " + str(self * getFactor(serotoninLevel, True)) + "ng")
        print("Current SEROTONIN level: " + str(Serotonin.serotoninLevel))

    def levelDown(self: float):
        serotoninLevel = Serotonin.serotoninLevel
        Serotonin.serotoninLevel = serotoninLevel - (self * getFactor(serotoninLevel))
        print("SEROTONIN level changed to down on " + str(self * getFactor(serotoninLevel)) + "ng")
        print("Current SEROTONIN level: " + str(Serotonin.serotoninLevel))

    def selfControl(self: float):
        while True:
            serotoninLevel = Serotonin.serotoninLevel
            Serotonin.serotoninLevel = serotoninLevel - (self * getSelfChangingFactor(serotoninLevel))
            print("Current SEROTONIN level: " + str(Serotonin.serotoninLevel))
            sleep(0.33)

    @staticmethod
    def getLevel():
        return Serotonin.serotoninLevel
