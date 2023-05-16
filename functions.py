def get_todos(filepath='todos.txt'):
    """Gets the list of items in the file passed as input"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath2='todos.txt'):
    """Writes todo items to the list in the text file passed"""
    with open(filepath2, 'w') as file_local2:
        file_local2.writelines(todos_arg)


#print(__name__)
if __name__ == "__main__":
    print("hello from Functions.py!")