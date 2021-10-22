class Vector3:
    x: float = 0
    y: float = 0
    z: float = 0


    def __init__(self, x = 0.0, y = 0.0, z = 0.0):
        self.x = x
        self.y = y
        self.z = z


    def scale(self, factor):
        self.x *= factor
        self.y *= factor
        self.z *= factor


    def __add__(self, p2):
        dupe = Vector3(self.x, self.y, self.z)

        dupe.x += p2.x
        dupe.y += p2.y
        dupe.z += p2.z

        return dupe
