import math

class Missile():
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def GetDistance(self, otherMissile):
        distance = math.sqrt((self.x - otherMissile.x)**2 + (self.y - otherMissile.y)**2)

        return distance