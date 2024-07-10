# to_do_list.py

# Define the list to store tasks
tasks = []

def display_menu():
    print("\nTo-Do List Application")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

def view_tasks():
    if not tasks:
        print("\nNo tasks in the list.")
    else:
        print("\nTasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def add_task():
    task = input("\nEnter the task: ")
    tasks.append(task)
    print(f"Task '{task}' added.")

def delete_task():
    if not tasks:
        print("\nNo tasks to delete.")
    else:
        view_tasks()
        try:
            task_index = int(input("\nEnter the task number to delete: ")) - 1
            if 0 <= task_index < len(tasks):
                removed_task = tasks.pop(task_index)
                print(f"Task '{removed_task}' deleted.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    while True:
        display_menu()
        choice = input("\nEnter your choice: ")
        if choice == '1':
            view_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            delete_task()
        elif choice == '4':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
