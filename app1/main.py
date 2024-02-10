# from functions import get_todos, write_todos
from app1 import functions as f
import time

txt = 'files/todos.txt'
todos_filename = "%s" % txt

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is ", now)

while True:
    # Get user input and strip space characters from the input
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]
        # if len(todo) = 0:
        # todo = input("Enter a todo: ") + "\n"
        todos = f.get_todos()

        todos.append(todo + '\n')

        f.write_todos(todos)

    elif user_action.startswith('show'):
        todos = f.get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            # number = int(input("Number of the todo to edit: "))
            number = number - 1

            todos = f.get_todos()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            f.write_todos(todos)

        except ValueError:
            print("Your command is not valid.")
            continue  # back to the beginning

    elif user_action.startswith('complete'):
        try:
            # number = int(input("Number of the todo to complete: "))
            number = int(user_action[9:])

            todos = f.get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            f.write_todos(todos)

            message = f"Todo {todo_to_remove} was removed from the list."

            print(message)
        except IndexError:
            print("No item with that number.")
            continue

    elif 'exit' in user_action:
        break
    else:
        print("Command is not valid.")

print("Bye!")
