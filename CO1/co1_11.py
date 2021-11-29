a = int(input("Enter First No:"))
b = int(input("Enter Second No:"))
c = int(input("Enter Third No:"))

if(a > b and a>c):
    print(a,"is largest")
elif(b > c):
    print(b,"is largest")
elif(c > a):
    print(c,"is largest")
