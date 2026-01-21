def copy_file(command: str) -> None:
    command, file_name, new_file_name = command.split()
    if file_name == new_file_name or command != "cp":
        return
    with (open(file_name, "r") as source,
          open(new_file_name, "w") as source_copy):
        source_copy.write(source.read())
