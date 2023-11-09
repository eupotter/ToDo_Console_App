from todo import ToDo
from todo_list import ToDoList

HELP = "--help"
ADD = "--add"
UPDATE = "--update"
DELETE = "--delete"
SHOWLIST = "--showlist"
EXIT = "exit"
SHOW_ONE = "--show"

AVAILABLE_COMMANDS = [f"todos {HELP}", 
                      f"todos {ADD} <title>, <description>", 
                      f"todos {UPDATE} <id>, title = <title>, description = <description>, status = <status>", 
                      f"todos {DELETE} <id>",
                      f"todos {SHOWLIST}",
                      f"todos {SHOW_ONE} <id>",
                      EXIT]

def main():
    todos = ToDoList()
    while True:
        command = input("Please enter your command:\n")
        if command == EXIT:
            break

        process_command(command,todos)
    
def process_command(command,todos):
    words = command.split(" ")
    if words[0] != "todos":
        print("Command invalid. Type todos --help for available commands")
        return
    if words[1] == HELP:
        for command in AVAILABLE_COMMANDS:
            print(command)
    elif words[1] == ADD:
        arguments = " ".join(words[2:])
        arguments = arguments.split(",")
        todos.add_todo(arguments[0], arguments[1])
    elif words[1] == SHOWLIST:
        for todo in todos.todos:
            todo.print()
    elif words[1] == UPDATE:
        todo_id = int(words[2].strip(", "))
        arguments = " ".join(words[3:])
        arguments = arguments.split(",")
        for argument in arguments:
            argument = argument.split("=")
            if argument[0].strip() == "title":
                todos.update_todo(todo_id,argument[1])
            elif argument[0].strip() == "description":
                todos.update_todo(todo_id, None, argument[1])
            elif argument[0].strip() == "status":
                todos.update_todo(todo_id, None, None, argument[1])
    elif words[1] == DELETE:
        todos.delete_todo(int(words[2]))
    elif words[1] == SHOW_ONE:
        todos.show_todo_by_id(int(words[2]))
    else:
        print(f"Unknow command {words[1]}. Type todos --help for available commands")

if __name__ == "__main__":
    main()