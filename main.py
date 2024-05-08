todos = []
while True:
    user_prompt = input("Type add, display, edit or exit : ")
    user_prompt = user_prompt.strip() #strip() : cuts out the extra white spaces at the beginning and at the end
    match user_prompt:
        case "add":
            todo = input("Enter todo: ")
            todos.append(todo)
            print("Successfully added........")
        case "display":
            print("The To-do list items are : ")
            for todo in todos:
                print(f"{todo}")
        case "edit":
            userIndex = int(input("Enter index to be edited "))
            if userIndex < len(todos):
                new = input("edit user todo: ")
                todos[userIndex] = new
            else:
                print("The index doesnt exist, Please check")
        case "exit":
            break
        case _:
            print("Invalid input. Please try again.")
