"""
todo_list = ["buy cereal","buy wheat flour"]
todo_list.append("take a walk") #adds element at the last
# todo_list.append("go to movie", "visit temple") only 1 value can be appended using append method
# #Throws TypeError: list.append() takes exactly one argument (2 given)
print("Initial list :",todo_list)
todo_list.insert(1,"visit temple") #inserts value at index 1
print("Inserting at position 1 :", todo_list)
# todo_list.extend(range(0,4)) ['buy cereal', 'visit temple', 'buy wheat flour', 'take a walk', 0, 1, 2, 3]
todo_list.extend(["buy honey", "buy maggie", "clean room"]) # add multiples values to the list
print("Accessing using index : ", todo_list[2], todo_list[-1])
print("The Todo List Is :\n " ,todo_list)
"""
n = list(range(1,11))
print(n) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n.pop() #by default removes the last element
print(n) #[1, 2, 3, 4, 5, 6, 7, 8, 9]

n.pop(5) #removes the 5th index element
print("5th indexed item(6) is removed using pop", n) # 5th indexed item(6) is removed using pop [1, 2, 3, 4, 5, 7, 8, 9]

del n[3] #deletes elements based on the index passed
print("Index 3 got deleted using del :", n) #Index 3 got deleted using del : [1, 2, 3, 5, 7, 8, 9]

n.remove(2) #removes by the value u passed first instance is removed
#if values doesnot exist throws ValueError: list.remove(x): x not in list
print(n) #[1, 3, 5, 7, 8, 9]
n.sort(reverse=True) #revese=True desc reverse=False asc
print(n) #[9, 8, 7, 5, 3, 1]
print(n.index(5)) #prints the index
# print(n.clear())
print(n)
