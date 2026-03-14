tasks = []

while True:
    print("\n===== TASK MANAGER =====")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter the task: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nYour tasks:")
            for i, task in enumerate(tasks):
                print(f"{i + 1}. {task}")

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to delete.")
        else:
            for i, task in enumerate(tasks):
                print(f"{i + 1}. {task}")
            try:
                num = int(input("Enter the task number to delete: "))
                tasks.pop(num - 1)
                print("Task deleted!")
            except:
                print("Invalid option.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Try again.")
