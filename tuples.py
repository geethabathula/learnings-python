#Creating a tuple
vowels=("a","e","i","o","u")
print(vowels)
#vowels[0]="u" #cannot be modified immutable
#TypeError: 'tuple' object does not support item assignment
print(vowels[-1])#Accessing tuple values
"""
#Lopping through for
for i in vowels[::-1]:
    print(i)   
"""
#Looping through while
v=len(vowels)-1
while v>=0:
    print(vowels[v])
    v=v-1
#Methods
print("Count of letter o in vowels:",vowels.count("o"))
print("index of letter o in vowels:",vowels.index("o"))

