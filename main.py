import json
from utils import load_tasks, save_tasks

print("Welcome to the Task Tracker App!")

def show_menu():
    print("\nTask Tracker")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Exit")

if __name__ == "__main__":
    tasks = load_tasks()

    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == '1':
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
        elif choice == '2':
            new_task = input("Enter new task: ")
            tasks.append(new_task)
            save_tasks(tasks)
        elif choice == '3':
            break
        else:
            print("Invalid option.")
