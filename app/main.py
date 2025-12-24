def copy_file(command: str) -> None:
    command = command.split()
    source_file_name = command[1]
    new_file_name = command[2]

    if source_file_name != new_file_name:
        with (open(source_file_name, "r") as source_file,
              open(new_file_name, "w") as new_file):
            new_file.write(source_file.read())
