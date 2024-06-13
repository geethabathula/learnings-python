print([x*5 for x in range(1,6)])

numbers=[1,2,3,4,5]
print([True if n%2==0 else False for n in numbers])

list1 = [1,2,3,4]
list2 = [3,4,5,6]
answer = [n for n in list1 if n in list1 and n in list2]
print(answer)

nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in nested_list:
    for j in i:
        print(f"{j} in {i}")