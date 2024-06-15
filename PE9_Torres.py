class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def inputSides(self):
        self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]

    def dispSides(self):
        for i in range(self.n):
            print("Side",i+1,"is",self.sides[i])

# class Triangle(Polygon):

#     def __init__(self):
#         Polygon.__init__(self,3)

#     def findArea(self):
#         a, b, c = self.sides
#         s = (a + b + c) / 2
#         area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
#         print('The area of the triangle is %0.2f' %area)

# t = Triangle()
# t.inputSides()
# t.dispSides()
# t.findArea()
# class Quadrilateral(Polygon):
#     def __init__(self):
#         super().__init__(4)

#     def findArea(self):
#         a, b, c, d = self.sides
#         area = (a * c) / 2
#         print('The area of the Rhombus is %0.2f' % area)


# r = Quadrilateral()
# r.inputSides()  
# r.dispSides()   
# r.findArea()


# class Square(Polygon):
#     def __init__(self):
#         Polygon.__init__(self,4)

#     def findArea(self):
#         side  = self.sides[0]
#         area = side * side
#         print('The area of the square is %d' %area)

# s= Square()
# s.inputSides()
# s.dispSides()
# s.findArea()

# import math
# class Circle(Polygon):
#     def __init__(self):
#         Polygon.__init__(self,1)

#     def findArea(self):
#         side = self.sides[0]
#         area =  math.pi * side * side
#         print('The Area of the circle is %0.2f' %area)

# c = Circle()
# c.inputSides()
# c.dispSides()
# c.findArea()


# class Rectangle(Polygon):
#     def __init__(self):
#         Polygon.__init__(self,4)

#     def findArea(self):
#         side1 = self.sides[0]
#         side2 = self.sides[1]
#         area = side1 * side2
#         print ('The are of the reactangle is %0.2f'%area)
# r = Rectangle()
# r.inputSides()
# r.dispSides()
# r.findArea()

