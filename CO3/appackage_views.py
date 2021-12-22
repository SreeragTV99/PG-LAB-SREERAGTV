from Graphics import circle
from Graphics import rectangle
from Graphics import cuboid
from Graphics import sphere

l = int(input("Enter length of rectangle :"))
b = int(input("Enter breadth of rectangle :"))
rectangle.rectangle(l,b)

r = int(input("Enter Radius of circle :"))
circle.circle(r)

l = int(input("Enter length of cuboid :"))
b = int(input("Enter breadth of cuboid :"))
h = int(input("Enter height of cuboid :"))
cuboid.cuboid(l,h,b)

r = int(input("Enter Radius of sphere :"))
sphere.sphere(r)
