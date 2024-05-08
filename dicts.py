dog = dict(name="Stella",age=5,isCute=True)
print(dog) #{'name': 'Stella', 'age': 5, 'isCute': True}
dogWalker = {"dogWalkerName":"Ruby Mitchell"}
print(dogWalker)
dogWalker.update(dog) #the dict is updated with dog dict items
dogWalker["name"]="Chikoo" #we can also overwrite the value using key
print(dogWalker)