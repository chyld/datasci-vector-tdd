class Vector:
    def __init__(self, *nums):
        self.storage = nums
        self.dim = len(nums)

    def __add__(self, other):
        nums = [self.storage[i] + other.storage[i] for i in range(self.dim)]
        return Vector(*nums)

    def __mul__(self, other):
        if isinstance(other, Vector):
            products = [a * b for a, b in zip(self.storage, other.storage)]
            return float(sum(products))
        else:
            nums = [n * other for n in self.storage]
            return Vector(*nums)

    def norm(self):
        return (self * self) ** 0.5

    def __str__(self):
        return "Vector: {}".format(self.storage)

    def __repr__(self):
        return self.__str__()
