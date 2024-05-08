s = set({1,2,3})
print(s,type(s))

#unordered and no duplicates
s2 = {"a","a","b","c"} #{'a', 'c', 'b'}
"""
#looping on sets
for i in s2:
    print(i)

"""
#Set Methods
s2.add("d")
s2.add("c")#doesnot throw error but it doesn't show up
print(s2)
s2.remove("c")
print(s2)
#if u try to remove unexisting value it throws keyError
#s2.remove("c") #KeyError: 'c' inorder to avoid this error u can use discard method
s2.discard("c")
print(s2)

#Converting set to a list
list = list(s2)
print(list)
