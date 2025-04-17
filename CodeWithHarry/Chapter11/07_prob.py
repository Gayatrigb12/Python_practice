class Vector:
    def __init__(self, list):
        self.list = list

    def __len__(self):
        return len(self.list)
v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6 ,7])
print("Length of (v1)",len(v1))
print("Length of (v2)",len(v2))
