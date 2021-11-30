word=input("Enter a word:")
print("Ordinal values corresponding to each element is:")
for i in word:
    print(i,end=":")
    print(ord(i),end=" ")