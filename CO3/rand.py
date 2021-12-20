import random

print(random.random())

print("===============================")

mylist = ["apple", "banana", "cherry"]
random.shuffle(mylist)
print(mylist)

print("===============================")

random.seed(10)
print(random.random())

print("===============================")

mylist = ["apple", "banana", "cherry"]
print(random.choice(mylist))

print("===============================")

print(random.randrange(3, 9))