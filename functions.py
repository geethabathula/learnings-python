#default parameters
def power_Of(num,p=2):
    return num**p
print(power_Of(2,6))#2**6 = 64
print(power_Of(3))#3**2 = 9

#keyword arguments
print(power_Of(num=4,p=3)) #4**3 = 64
print(power_Of(p=5,num=2)) #2**5 = 32



"""
name=input()
#Defining a function
def sing_happy_birthday(name):
    print(f"Happy Birthday {name}")
sing_happy_birthday(name) #Calling a function



def s():
    return 7 ** 2


v = s()
print(v)#49
"""