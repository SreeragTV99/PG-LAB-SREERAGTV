class rectangle():
    def __init__(self,breadth,length):
        self.breadth=breadth
        self.length=length
    def area(self):
        return self.breadth*self.length
    def perimeter(self):
        return 2*self.breadth*self.length

a=int(input("Enter length of First rectangle: "))
b=int(input("Enter breadth of First rectangle: "))
obj1=rectangle(a,b)
print("Area of rectangle :",obj1.area())
print("Perimeter of rectangle :",obj1.perimeter())
print("---------------------------------------")
c=int(input("Enter length of Second rectangle: "))
d=int(input("Enter breadth of Second rectangle: "))
obj2=rectangle(c,d)
print("Area of rectangle :",obj2.area())
print("Perimeter of rectangle :",obj2.perimeter())
print("---------------------------------------")

if(obj1.area()>obj2.area()):
    print(obj1.area(), "is largest.(First Rectangle)")
else:
    print(obj2.area(), "is largest.(Second Rectangle)")