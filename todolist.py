class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_tasks(self, task):
        self.tasks.append(task)
        print(f'Task "{task}" added to the to-do list.')

    def view_tasks(self):
        if not self.tasks:
            print('No tasks in the to-do list.')
        else:
            print('To-Do List:')
            for index, task in enumerate(self.tasks, start=1):
                print(f'{index}. {task}')

    def mark_as_completed(self,task_index):
        if 1 <= task_index <= len(self.tasks):
            completed_task = self.tasks.pop(task_index - 1)
            print(f'Task "{completed_task}" marked as completed.')
        else:
            print('Invalid task index.')

def main():
    todo_list = ToDoList()

    while True:
        print('Menu:')
        print('Add Task')
        print('View Tasks')
        print('Mark Task as Completed')
        print('Exit')
        choice = input('Enter your choice')
        if choice == '1':
            task = input('Enter the task: ')
            todo_list.add_tasks(task)
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            todo_list.view_tasks()
            task_index = int(input('Enter the index of the task to mark as completed: '))
            todo_list.mark_as_completed(task_index)
        elif choice == '4':
            print('tasks have been completed')
            break
        else:
            print('Invalid choice')

if __name__ == "__main__":
    main()
