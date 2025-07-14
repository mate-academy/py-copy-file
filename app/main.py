def copy_file(command: str) -> None:
    command_parts = command.split(" ")

    if len(command_parts) == 3 and command_parts[0] == "cp":
        file_name = command_parts[1]
        copy_file_name = command_parts[2]

        if file_name != copy_file_name:
            try:
                with (open(file_name, "r") as file,
                      open(copy_file_name, "w") as new_file):
                    for line in file:
                        new_file.write(line)
            except FileNotFoundError:
                pass
