class Cube:
    def __init__(self, side_length):
        self.side_length = side_length

    def volume(self):
        return self.side_length ** 3

    def surface_area(self):
        return 6 * (self.side_length ** 2)

    def mass(self):
        return self.volume() * 2.7

    def __str__(self):
        return f"Cube with side length {self.side_length}, volume of {self.volume()}, surface area of {self.surface_area()}, and mass of {self.mass()}"


rock = Cube(3)

print(rock)


def areal_density(cube):
    a_d = cube.mass() / cube.surface_area()
    return a_d


print(f"Areal density of the cube: {areal_density(rock)}")
