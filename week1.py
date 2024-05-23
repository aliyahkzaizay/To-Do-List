
def commands():
    print("\nCommands:")
    print("1. Add Task ")
    print("2. Delete Task")
    print("4. Mark as done")
    print("5. Print Tasks")
    command = input("What would you like to do? Enter your choice: (Enter 0 to stop): ")

    return command


#Get user name
name = input('Enter your name: ')
print(f"\nWelcome {name}!")

print("Here is your To-Do List: ")

toDoList = [];

if not toDoList:
    
    print("\nOh,your list is empty!")
    


while True:
    command = commands()

    if command == "0":
 
        break
    elif command == "1":
        add = input("Enter to-do: ")
        toDoList.append((add, "Not Done"))
        print("Task added!")
    elif command == "2":
       if toDoList:
        print("\nYour current To-Do List:")
        for index, (task, completion) in enumerate(toDoList):
                print(f"Index {index}: {task} - {completion}")
        try:
            index = int(input("Enter index to be deleted: "))
            if 0 <= index < len(toDoList):

                toDoList.pop(index)
                print("Deletion successful.")
            else:
                print("Error: Index out of range.")
        except ValueError:
            print("Error: Please enter a valid integer.")
       else:
        print("Your to-do list is empty, nothing to delete.")
    elif command == "4":
        print("\nYour current To-Do List:")
        for index, item in enumerate(toDoList):
                print(f"Index {index}: {item}")

        taskIndex = input("Which task do you wish to mark done? Enter index: ")

        toDoList[taskIndex][1] = "Done"
        print("Task marked as done!")
    elif command == "5":
        print("\nYour current To-Do List:") 
        for index, (task, completion) in enumerate(toDoList):
                print(f"Index {index}: {task} - {completion}")
        
    else:
       print("Error, that is not a supported command.")  

print("Goodbye!")