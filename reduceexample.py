from functools import reduce

l = [1,2,3,4]
product = reduce(lambda x, y: x * y, l)
print(product)
l2 = [2,3,1]

total = reduce(lambda x,y: x//y, l2,25)
print(total)