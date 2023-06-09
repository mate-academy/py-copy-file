def copy_file(command: str) -> None:
    list_command = command.split()
    if list_command[0] == "cp" and len(list_command) == 2:
        old_file = list_command[1]
        new_file = old_file.split(".")[0] + "-copy.txt"
        with open(old_file, "r") as file_in, open(new_file, "w") as file_out:
            file_out.write(file_in.read())
    if list_command[0] == "cp" and len(list_command) == 3:
        old_file = list_command[1]
        new_file = list_command[2]
        if old_file == new_file:
            return
        with open(old_file, "r") as file_in, open(new_file, "w") as file_out:
            file_out.write(file_in.read())
