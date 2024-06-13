ips = ['100.122.133.105', '100.122.133.111']
prompt = int(input("Enter 0 or 1: "))
print(ips[prompt])

for i in range(1,6):
    print("\U0001f600"*i,i)

i=1
while i<6:
    print("\U0001f600"*i,i)
    i=i+1

filenames = ['document', 'report', 'presentation']
for i,file in enumerate(filenames):
    print(f"{i}-{file.capitalize()}.txt")