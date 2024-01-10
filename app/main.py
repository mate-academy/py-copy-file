def copy_file(command: str) -> None:
    ls_command = command.split()
    command_name, file_name, new_file_name = (
        ls_command[0], ls_command[1], ls_command[2])
    if file_name != new_file_name and command_name == "cp":
        with (open(file_name, "r") as source,
              open(new_file_name, "w") as new_file):
            new_file.write(source.read())
