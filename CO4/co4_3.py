class rectangle:
    def __init__(self,length,width):
        self.__length=length
        self.__width=width
    def __lt__(self,a1):
        area1=self.__length*self.__width
        area2=a1.__length*a1.__width
        if(area1<area2):
            return(True)
        else:
            return(False)
        
a1=int(input("Length of  First Rectangle:"))
b1=int(input("Width of First Rectangle:"))
r1=rectangle(a1,b1)

a2=int(input("\nLength of Second Rectangle:"))
b2=int(input("Width of Second Rectangle:"))
print("\n--------------------------------")
r2=rectangle(a2,b2)
if(r1<r2):
    print("\nSecond Rectangle is larger.")
else:
    print("\nFirst Rectangle is larger.")