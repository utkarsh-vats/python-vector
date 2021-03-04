from vector import Vector

a = Vector(3.54, 3.54)
b = Vector(5, 0)

print(a.mag())
c = a.copy()
print(c.toString())
d = b.copy()
d.printVect()
b.add(1, 2, 3)
b.printVect()
d.addVect(b)
d.printVect()
