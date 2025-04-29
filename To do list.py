tasks = []

def add_task():
    task = input("Enter the task: ")
    tasks.append({"task": task, "completed": False})
    print(f"Task '{task}' added.")

def view_tasks():
    if not tasks:
        print("Your to-do list is empty.")
    else:
        print("Your to-do list:")
        for index, task_dict in enumerate(tasks):
            status = "[X]" if task_dict["completed"] else "[ ]"
            print(f"{index + 1}. {status} {task_dict['task']}")

def mark_complete():
    if not tasks:
        print("Your to-do list is empty.")
        return
    view_tasks()
    try:
        task_index = int(input("Enter the number of the task to mark as complete: ")) - 1
        if 0 <= task_index < len(tasks):
            tasks[task_index]["completed"] = True
            print(f"Task '{tasks[task_index]['task']}' marked as complete.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def delete_task():
    if not tasks:
        print("Your to-do list is empty.")
        return
    view_tasks()
    try:
        task_index = int(input("Enter the number of the task to delete: ")) - 1
        if 0 <= task_index < len(tasks):
            deleted_task = tasks.pop(task_index)["task"]
            print(f"Task '{deleted_task}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

while True:
    print("\nOptions:")
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task as complete")
    print("4. Delete task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        mark_complete()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        print("Exiting the to-do list application. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
