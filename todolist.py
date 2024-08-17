tasks=[]

def addTask():
    task=input("Task to be added:")
    tasks.append(task)
    print(task,"has been added in the list.")

def deleteTask():
    viewTask()
    try:
        if tasks:
            taskToDelete = int(input("Choose the number of the task you want to delete: "))
            if taskToDelete <= len(tasks) and taskToDelete > 0:
                deleted_task = tasks.pop(taskToDelete - 1)
                print(f"Task '{deleted_task}' has been deleted from the list.")
            else:
                print("Invalid task number")
        else:
            print("Empty List")
    except ValueError:
        print("Invalid Input.")

def UpdateTask():
    viewTask()
    try:
        if tasks:
            taskToUpdate = int(input("Choose the number of the task you want to update: "))
            if 1 <= taskToUpdate <= len(tasks):
                updatedTask = input("Enter the updated task: ")
                tasks[taskToUpdate - 1] = updatedTask
                print(f"Task '{updatedTask}' has been updated in the list.")
            else:
                print("Invalid task number.")
        else:
            print("Empty List")
    except ValueError:
        print("Invalid Input.")

def viewTask():
    if not tasks:
        print("Empty List")
    else:
        for index, task in enumerate(tasks):
            print(index+1,task)

def markedTask():
    viewTask()  
    try:
        if tasks:
            taskToMark = int(input("Choose the number of the task you want to mark complete:"))
            if 1 <= taskToMark <= len(tasks):
                tasks[taskToMark - 1] += ' ✓'  
                print(f"Task '{tasks[taskToMark - 1]}' has been marked complete.")
            else:
                print("Invalid task number.")
        else: 
            print("Empty List")
    except ValueError:
        print("Invalid Input.")

def trackTask(): #to track completed and incompleted tasks
    if not tasks:
        print("Empty List")
        return
    print("A. Tasks Completed")
    print("B. Tasks Yet to Complete")
    c = input("Enter the choice: ").strip().upper()

    if c == 'A':
        print("Completed Tasks:")
        for index, task in enumerate(tasks, start=1):
            if '✓' in task:
                print(index, task)
        if all('✓' not in task for task in tasks):
            print("No completed tasks.")
            
    elif c == 'B':
        print("Incomplete Tasks:")
        for index, task in enumerate(tasks, start=1):
            if '✓' not in task:
                print(index, task)
        if all('✓' in task for task in tasks):
            print("All tasks are completed.")
    else:
        print("Invalid choice.")

if __name__=="__main__":
    print("TO-DO LIST")
    while True:
        print("\nChoose the option to be performed:")
        print("----------------------------------------------------------")
        print("1. {:<25} {}".format("Add a new task:", "2. Delete an existing task:"))
        print("3. {:<25} {}".format("Update a task:", "4. View a task:"))
        print("5. {:<25} {}".format("Mark task as completed:", "6. Track the tasks:"))
        print("7. {:<25}".format("Exit:"))

        choice=input("Your Choice [1/2/3/4/5/6/7]:")

        if choice=='1': 
            addTask()
        elif choice=='2':
            deleteTask()
        elif choice=='3':
            UpdateTask()
        elif choice=='4':
            viewTask()
        elif choice=='5':
            markedTask()
        elif choice=='6':
            trackTask()
        elif choice=='7':
             break
        else:
            print("Wrong Input..")
    print("Exiting...")
        