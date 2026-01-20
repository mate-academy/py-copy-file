def copy_file(command: str) -> None:
    command_list = command.split(" ")
    if len(command_list) == 3 and command_list[0] == "cp":
        try:
            file_name = command_list[1]
            new_file_name = command_list[2]
            if file_name != new_file_name:
                with open(file_name, "r") as file, \
                     open(new_file_name, "w") as new_file:
                    content = file.read()
                    new_file.write(content)
        except FileNotFoundError:
            return
