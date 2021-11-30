lst1=[12,3,4,3,6,7,9,11,23,5]
lst2=[32,3,35,7,5,20,65,1]
s=int(0) 
c=int(0)

if len(lst1)==len(lst2):
  print("Lists are of same length") 
else:
  print("Lists are of different length")
  
for i in range(0,len(lst1) and len(lst2)):
    s = lst1[i]
    c = c+lst2[i]
if(s==c):
  print("equal sum")
else:
  print("not same sum")

print("Elements that matched are:") 
l=[]
for i in range(0,len(lst1)):
  for j in range(0,len(lst2)):
    if lst1[i]==lst2[j]:
        l.append(lst1[i] and lst2[j]) 
    else:
      continue
print(l)