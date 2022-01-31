f1 = open("firstfile.txt","r")
f2=open("odd.txt","w")
for x in f1:
    print(x)
print("---------------")
f1.seek(0,0)    
ff=f1.readlines()
for x in range(0,len(ff)):
    if(x%2==0):
        f2.write(ff[x])
        print(ff[x])
print("---------------")
