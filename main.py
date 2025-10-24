import json
import os

filepath = 'tasks.json'

def load_tasks():
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as file:
            return json.load(file)
    return []
    
def get_unfinished_tasks(tasks):
    return [task for task in tasks if not task['done']]

def finish_task(tasks, task_id):
    if not (1 <= task_id <= len(tasks)):
        print("Invalid task ID!")
        return False
    tasks[task_id - 1]['done'] = True
    save_tasks(tasks)
    print(f"Task '{tasks[task_id - 1]['title']}' completed successfully! ✅")
    return True

def delete_task(tasks, task_id):
    if not (1 <= task_id <= len(tasks)):
        print("Invalid task ID!")
        return False
    deleted_task = tasks.pop(task_id - 1)
    save_tasks(tasks)
    print(f"Task '{deleted_task['title']}' deleted successfully! 🗑️")
    return True

def add_task(tasks, title):
    if not title.strip():
        print("Task title cannot be empty!")
        return False
    new_task = {"title": title.strip(), "done": False}
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task '{title}' added successfully! 📝")
    return True

def save_tasks(tasks):
    try:
        with open(filepath, "w", encoding="utf-8") as file:
            json.dump(tasks, file, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"Error saving file: {e}")

def show_menu():
    print("\n🌟 Welcome! 🌟")
    print("1. Show all tasks")
    print("2. Show unfinished tasks")
    print("3. Add a new task")
    print("4. Complete a task")
    print("5. Delete a task")
    print("6. Exit")
    
    try:
        choice = int(input("Choose an option [1-6]: "))
        if choice not in range(1, 7):
            print("Please enter a number between 1 and 6!")
            return None
        return choice
    except ValueError:
        print("Please enter a number only!")
        return None

def show_tasks(tasks):
    print("")
    if not tasks:
        print("No tasks available! 😴")
        return
    for index, task in enumerate(tasks, 1):
        status = "✅" if task['done'] else "⏳"
        print(f"{index}. {task['title']} {status}")

def close_app():
    print("Goodbye, see you soon! 👋")

def main():
    tasks = load_tasks()
    
    while True:
        choice = show_menu()
        if choice is None:
            continue

        if choice == 1:
            show_tasks(tasks)

        elif choice == 2:
            unfinished_tasks = get_unfinished_tasks(tasks)
            show_tasks(unfinished_tasks)

        elif choice == 3:
            title = input("Enter the task title: ")
            add_task(tasks, title)

        elif choice == 4:
            if not tasks:
                print("No tasks available! 😴")
            else:
                show_tasks(tasks)
                try:
                    task_id = int(input("Enter the ID of the completed task: "))
                    finish_task(tasks, task_id)
                except ValueError:
                    print("Please enter a number only!")

        elif choice == 5:
            if not tasks:
                print("No tasks available! 😴")
            else:
                show_tasks(tasks)
                try:
                    task_id = int(input("Enter the ID of the task to delete: "))
                    delete_task(tasks, task_id)
                except ValueError:
                    print("Please enter a number only!")

        elif choice == 6:
            close_app()
            break

if __name__ == "__main__":
    main()