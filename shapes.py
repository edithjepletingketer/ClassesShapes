class Circle:
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        radius = self.radius
        a = (22/7)*radius*radius
        print(a)    
    def circumference(self):
        radius = self.radius
        C = 2*(22/7)*radius
        print(C)
class Square:
    def __init__(self,width):
        self.width = width
    def area(self):
        width = self.width
        A = width*width
        print(A)
    def perimeter(self):
        width = self.width
        P = 4*width
        print(P)
class Rectangle:
    def __init__(self,width,length):
        self.width = width
        self.length = length
    def area(self):
        width = self.width
        length = self.length
        A = width * length
        print(A)    
    def perimeter(self):
        width = self.width
        length = self.length
        P = 2(width+length)
        print(P)
class Sphere:
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        radius = self.radius
        A = 4*(22/7)*radius*radius
        print(A)
    def volume(self):
        radius = self.radius
        V = (4/3)*(22/7)*radius*radius*radius
        print(V)                            
