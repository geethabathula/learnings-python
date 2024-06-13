l=[1,2,34,-9,-4,2]
remove_negatives = list(filter(lambda i:i>=1,l))

print(remove_negatives)

names = ['Lassie', 'Colt', 'Rusty']

#filter and map example
samp = f"Your instructor is "
print(list(map(lambda n:f"Your instructor {n}",filter(lambda i:len(i)<5,names))))

print([f"Your instructor {name}" for name in names if len(name)<5])