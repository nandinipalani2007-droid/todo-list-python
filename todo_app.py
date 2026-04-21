try:
    with open("tasks.txt", "r") as file:
        task_list = [task.strip() for task in file.readlines()]
except FileNotFoundError:
    task_list = []

def display_menu():
    print("\n" + "="*30)
    print("TODO LIST MANAGER")
    print("="*30)
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Delete Task")
    print("4. Mark as Completed")
    print("5. Exit")
    print("="*30)

def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

def show_tasks(tasks):
    print("\nYOUR TASKS:")
    print("-" * 40)
    if not tasks:
        print("No tasks yet! Add some to get started.")
    else:
        for index, task in enumerate(tasks, 1):
            print(f"{index}. {task}")
    print("-" * 40)

while True:
    display_menu()
    choice = input("Enter your choice (1-5): ").strip()
    
    if choice == "1":
        new_task = input("\nWhat task would you like to add? ").strip()
        if new_task:
            task_list.append(new_task)
            save_tasks(task_list)
            print(f"'{new_task}' added successfully!")
        else:
            print("Task cannot be empty!")
    
    elif choice == "2":
        show_tasks(task_list)
    
    elif choice == "3":
        show_tasks(task_list)
        if task_list:
            try:
                index = int(input("\nEnter task number to delete: "))
                if 1 <= index <= len(task_list):
                    removed_task = task_list.pop(index - 1)
                    save_tasks(task_list)
                    print(f"'{removed_task}' deleted successfully!")
                else:
                    print("Invalid task number!")
            except ValueError:
                print("Please enter a valid number!")
        else:
            print("No tasks to delete!")
    
    elif choice == "4":
        show_tasks(task_list)
        if task_list:
            try:
                index = int(input("\nEnter task number to mark as completed: "))
                if 1 <= index <= len(task_list):
                    task_list[index - 1] = "[✔] " + task_list[index - 1]
                    save_tasks(task_list)
                    print("Task marked as completed!")
                else:
                    print("Invalid task number!")
            except ValueError:
                print("Please enter a valid number!")
        else:
            print("No tasks available!")
    
    elif choice == "5":
        print("\nThanks for using Todo Manager! Goodbye!")
        break
    
    else:
        print("\nInvalid choice! Please select 1-5.")
    
    input("\nPress Enter to continue...")