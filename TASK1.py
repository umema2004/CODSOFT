class Task:
    def __init__(self, description, completed=False):
        self.description = description
        self.completed = completed

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        self.tasks.append(Task(description))

    def view_tasks(self):
        for i, task in enumerate(self.tasks, start=1):
            status = "Done" if task.completed else "Pending"
            print(f"{i}. [{status}] {task.description}")

    def mark_task_as_done(self, task_index):
        self.tasks[task_index - 1].completed = True

    def remove_task(self, task_index):
        del self.tasks[task_index - 1]

    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            for task in self.tasks:
                f.write(f"{task.description},{task.completed}\n")

    

def main():
    todo_list = ToDoList()
    while True:
        print("---- WELCOME TO UMEMA'S TO DO LIST ----")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Remove Task")
        print("5. Save Tasks to File")
        # print("6. Load Tasks from File")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            description = input("Enter task description: ")
            todo_list.add_task(description)
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            task_index = int(input("Enter task number to mark as done: "))
            todo_list.mark_task_as_done(task_index)
        elif choice == '4':
            task_index = int(input("Enter task number to remove: "))
            todo_list.remove_task(task_index)
        elif choice == '5':
            filename = input("Enter filename to save: ")
            todo_list.save_to_file(filename)
            print("Tasks saved to file.")
        # elif choice == '6':
        #     filename = input("Enter filename to load: ")
        #     todo_list.load_from_file(filename)
        #     print("Tasks loaded from file.")
        elif choice == '0':
            break
        else:
            print("Invalid input try again :(")

if __name__ == "__main__":
    main()
