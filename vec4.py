class Vector4:
    x: float = 0
    y: float = 0
    z: float = 0
    w: float = 0


    def __init__(self, x = 0.0, y = 0.0, z = 0.0, w = 0.0):
        self.x = x
        self.y = y
        self.z = z
        self.w = w


    def sum(self):
        return self.x + self.y + self.z + self.w


    def __mul__(self, rhs):
        return Vector4(self.x * rhs.x, self.y * rhs.y, self.z * rhs.z, self.w * rhs.w)