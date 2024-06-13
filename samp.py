

names = [{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]

def extract_full_name(name):
    s = list(map (lambda x: x["first"]+" "+x["last"],name))
    return s

print(extract_full_name(names) )# ['Elie Schoppik', 'Colt Steele']

def triple_and_filter(lists):
    return [v*3 for v in lists if v%4==0]
print(triple_and_filter([1, 2, 3, 4]))  # [12]
print(triple_and_filter([6, 8, 10, 12]) ) # [24,36]
# args example
# def sum(*args):
#     total = 0
#     for i in args:
#         total = total + 1
#     return print(total)
# sum(1,223,3434)
# sum(23,45,768,89)

# import random as r
#
# print("Guessing Game b/w 1 to 10")
# random = r.randint(1,10)
# userEntry = int(input("Enter Number: "))
# while userEntry != random:
#     userEntry = int(input("Enter Number: "))
# print("You guessed it correct")