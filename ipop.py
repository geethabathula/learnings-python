#Creating a File practice.txt
#myFile = open("practice.txt","x+")
#myFile.write("Hi everyone\nwe are learning File I/O\nusing Java.\nI like programming in Java")
#myFile.close()

with open("D:\\Python\\ToDoApp\\venv\\practice.txt","r") as file:
    data = file.readlines()
    print(data)
    file.close()
