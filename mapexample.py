def decrement_list(args):
    l=[]
    for i in args:
        l.append(i-1)
    return l
regular = decrement_list([1,2,3])
print(regular)

#using map
maps=list(map(lambda n:n-1,[1,2,3]))
print(maps)
help(map)