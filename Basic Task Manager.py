import json
import os

TASKS_FILE = 'tasks.json'

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file)

def add_task(tasks, task_description):
    tasks.append({"description": task_description, "done": False})
    save_tasks(tasks)

def list_tasks(tasks):
    for idx, task in enumerate(tasks, start=1):
        status = "Done" if task["done"] else "Not Done"
        print(f"{idx}. {task['description']} [{status}]")

def mark_task_done(tasks, task_index):
    if 0 <= task_index < len(tasks):
        tasks[task_index]["done"] = True
        save_tasks(tasks)

def delete_task(tasks, task_index):
    if 0 <= task_index < len(tasks):
        tasks.pop(task_index)
        save_tasks(tasks)

def main():
    tasks = load_tasks()

    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            task_description = input("Enter task description: ")
            add_task(tasks, task_description)
        elif choice == '2':
            list_tasks(tasks)
        elif choice == '3':
            task_index = int(input("Enter task number to mark as done: ")) - 1
            mark_task_done(tasks, task_index)
        elif choice == '4':
            task_index = int(input("Enter task number to delete: ")) - 1
            delete_task(tasks, task_index)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()