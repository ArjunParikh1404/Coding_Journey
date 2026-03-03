# A basic CLI To-Do List app that lets users manage tasks interactively.

tasks = []

while True:
    
    print("\n1. Add Task\n2. View Tasks\n3. Delete Task\n4. Exit")
    choice = input("Choose: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        
    elif choice == "2":
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")
            
    elif choice == "3":
        num = int(input("Enter task number to delete: "))
        tasks.pop(num-1)
        
    elif choice == "4":
        break
