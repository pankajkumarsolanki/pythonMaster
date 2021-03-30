class Sphere():
    pi = 3.14
    def __init__(self, radius):
        self.radius = radius

    def volume(self):
        print((4/3)*self.pi*self.radius**3)

    def surface_area(self):
        print(4*self.pi*self.radius**2)



s = Sphere(1)
s.volume()
s.surface_area()