import random
#shuffle
mylist = ["apple", "banana", "cherry"]
random.shuffle(mylist)

print(mylist)

#zip funtion
l1=[1,2,3]
l2=["geetha","swetha","ramlakshmi"]
print("zip",zip(l1,l2))
for i in zip(l1,l2):
    print(i)

#randint
print("Randint",random.randint(1,10))