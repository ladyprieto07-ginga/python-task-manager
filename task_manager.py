import json



try:
    with open("tasks.json", "r") as file:
        tasks = json.load(file)
except:
    tasks = []
    
def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)
        
def show_menu():
    print("\n--- TASK MANAGER ---")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Exit")

def add_task():
    save_tasks()
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added!")

def view_tasks():
    if len(tasks) == 0:
        print("No tasks available.")
    else:
        print("\nYour tasks:")
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task}")

def delete_task():
    view_tasks()
    save_tasks()
    try:
        task_number = int(input("Enter the task number to delete: "))
        tasks.pop(task_number - 1)
        print("Task deleted!")
    except:
        print("Invalid task number.")

while True:
    show_menu()
    choice = input("Choose an option: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid option.")