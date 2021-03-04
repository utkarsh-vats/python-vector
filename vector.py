from math import sqrt
class Vector:
    def __init__(self, X, Y, Z = 0):
        self.x = X
        self.y = Y
        self.z = Z
    
    def mag(self):
        return sqrt(self.x**2 + self.y**2 + self.z**2)

    def magSq(self):
        return self.x**2 + self.y**2 + self.z**2

    def normalize(self):
        mag = self.mag()
        self.x = self.x / mag
        self.y = self.y / mag
        self.z = self.z / mag

    def dot(self, vectB):
        return (self.x * vectB.x + self.y * vectB.y + self.z * vectB.z)

    def cross(self, vectB):
        a = self.y * vectB.z - self.z * vectB.y
        b = self.z * vectB.x - self.x * vectB.z
        c = self.x * vectB.y - self.y * vectB.x
        return Vector(a, b, c)

    def printVect(self):
        print("(" + "{}, {}, {}".format(self.x, self.y, self.z) + ")")

    def toString(self):
        return "(" + "{}, {}, {}".format(self.x, self.y, self.z) + ")"

    def set(self, x, y, z = None):
        self.x = x
        self.y = y
        if z != None:
            self.z = z

    def copy(self):
        return Vector(self.x, self.y, self.z)

    def addVect(self, vectB):
        self.x = self.x + vectB.x
        self.y = self.y + vectB.y
        self.z = self.z + vectB.z
    
    def add(self, x, y,  z):
        self.x = self.x + x
        self.y = self.y + y
        self.z = self.z + z