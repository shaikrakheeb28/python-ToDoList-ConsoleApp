# to_do_list.py

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "done": False})
        print(f'Task added: {task}')

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        for idx, task in enumerate(self.tasks):
            status = "Done" if task["done"] else "Pending"
            print(f"{idx + 1}. {task['task']} - {status}")

    def mark_done(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["done"] = True
            print(f"Marked task {index + 1} as done.")
        else:
            print("Invalid task number.")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            removed = self.tasks.pop(index)
            print(f"Deleted task: {removed['task']}")
        else:
            print("Invalid task number.")


def main():
    todo = ToDoList()
    while True:
        print("\n--- To-Do List Menu ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")
        if choice == '1':
            task = input("Enter task: ")
            todo.add_task(task)
        elif choice == '2':
            todo.view_tasks()
        elif choice == '3':
            idx = int(input("Enter task number to mark done: ")) - 1
            todo.mark_done(idx)
        elif choice == '4':
            idx = int(input("Enter task number to delete: ")) - 1
            todo.delete_task(idx)
        elif choice == '5':
            print("Exiting To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
