def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) == 3:
        command_name, file_name, new_file_name = parts
        if file_name != new_file_name and command_name == "cp":
            with (open(file_name, "r") as source,
                  open(new_file_name, "w") as new_file):
                new_file.write(source.read())
