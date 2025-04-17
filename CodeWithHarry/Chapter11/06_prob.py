class Vector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k

    def __add__(self, v2):
        return Vector(self.i + v2.i, self.j + v2.j, self.k + v2.k)

    def __mul__(self, v2):
        # Dot product
        return self.i * v2.i + self.j * v2.j + self.k * v2.k

    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"

v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

print("Add (V1 , V2):", v1 + v2)
print("Dot Product (V1 , V2):", v1 * v2)
