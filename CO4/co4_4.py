class Time:
    def __init__(self,hour,minute,second):
        self.__hour=hour
        self.__minute=minute
        self.__second=second
    def __add__(self,h):
        second=self.__second+h.__second
        minute=self.__minute+h.__minute
        hour=self.__hour+h.__hour
        if(second>60):
            second=second-60
            minute=minute+1
        if(minute>60):
            minute=minute-60
            hour=hour+1
        return hour,minute,second
print("---Enter First Time---\n")
h1=int(input("Enter The Hour : "))
m1=int(input("Enter The Minute : "))
s1=int(input("Enter The Second : "))

t1=Time(h1,m1,s1)

print("\n---Enter Second Time---\n")
h2=int(input("Enter The Hour : "))
m2=int(input("Enter The Minute : "))
s2=int(input("Enter The Second : "))

t2=Time(h2,m2,s2)

hr,min,sec=t1+t2
print("--------------------")
print(hr,end=":")
print(min,end=":")
print(sec,end=" ")