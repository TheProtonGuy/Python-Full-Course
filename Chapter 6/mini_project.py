"""
Create a Python program that lets the user add, 
remove, and display items in a to-do list.
"""

my_todolist_items = []
print("1. Display all items\n2. Add new item\n3. Delete an item\n4. Exit")

while True:
    operation = int(input("Select operation: "))

    if operation == 1:
        print("\nBelow are your todo list items")
        for index, item in enumerate(my_todolist_items):
            print(f"{index}. {item}")

    elif operation == 2:
        todo_item = input("Enter todo item: ")
        my_todolist_items.append(todo_item)

    elif operation == 3:
        item_id = int(input("Enter id of item to be deleted: "))
        my_todolist_items.pop(item_id)

    elif operation == 4:
        break