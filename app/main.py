def copy_file(command: str) -> None:
    command_split = command.split(" ")
    if len(command_split) == 3 and command_split[0] == "cp":
        file_name = command_split[1]
        new_file_name = command_split[2]
        if file_name != new_file_name:
            try:
                with (
                    open(file_name, "r") as old_file,
                    open(new_file_name, "w") as new_file
                ):
                    for line in old_file:
                        new_file.write(line)
            except FileNotFoundError:
                print(f"{file_name} does not exist")
