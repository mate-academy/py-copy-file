import os


# variant 1
def copy_file_1(command: str) -> None:
    splited_command = command.split(" ")
    if splited_command[1] == splited_command[2]:
        return
    # src = "file.txt"
    # dest = "new_file.txt"
    os.system(command)


# variant 2
def copy_file_2(command: str) -> None:
    splited = command.split(" ")
    source = splited[1]
    destination = splited[2]
    if source == destination:
        return
    with open(source, "r") as file_in, open(destination, "w") as file_out:
        text_to_copy = file_in.read()
        file_out.write(text_to_copy)

# there can be a third variant that uses shutil module
