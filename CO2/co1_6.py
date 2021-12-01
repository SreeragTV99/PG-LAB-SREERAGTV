string=str(input("Enter the string : "))
freq = {}
for i in string:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
print("Count of all characters : "+ str(freq))
