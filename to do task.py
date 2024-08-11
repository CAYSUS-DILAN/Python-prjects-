# To-Do List Application

tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added.")

def view_tasks():
    if tasks:
        print("Your tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    else:
        print("No tasks.")

def mark_task_done(task_index):
    if task_index >= 1 and task_index <= len(tasks):
        task = tasks[task_index - 1]
        print(f"Task '{task}' marked as done.")
        tasks.pop(task_index - 1)
    else:
        print("Invalid task index.")

def remove_task(task_index):
    if task_index >= 1 and task_index <= len(tasks):
        task = tasks[task_index - 1]
        print(f"Task '{task}' removed.")
        tasks.pop(task_index - 1)
    else:
        print("Invalid task index.")

def print_menu():
    print("\nMenu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Remove Task")
    print("5. Exit")

def main():
    while True:
        print_menu()
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            task = input("Enter task: ")
            add_task(task)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            task_index = int(input("Enter task index to mark as done: "))
            mark_task_done(task_index)
        elif choice == '4':
            task_index = int(input("Enter task index to remove: "))
            remove_task(task_index)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()
               