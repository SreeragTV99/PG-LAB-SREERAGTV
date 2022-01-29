#Write a Python program to write a Python dictionary to a csv file. After writing the CSV file read the CSV file and display the content.

import csv

header=["place","name","age"]
with open("test1.csv","w") as file:
    write=csv.DictWriter(file,fieldnames=header)
    write.writeheader()
    limit = int(input("Enter the No.of lines you want to enter:"))
    for i in range(limit):
        row_str = input("Enter the data in order (place,name,age) separated by comma:")
        row_lst = row_str.split(",")
        write.writerow({"place":row_lst[0],"name":row_lst[1],"age":row_lst[2]})
with open("test1.csv", 'r') as file:
    read=csv.DictReader(file);
    for i in read:
        print(dict(i))