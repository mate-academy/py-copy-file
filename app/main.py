def copy_file(command: str) -> None:
    command, old_file_name, new_file_name = command.split()

    if command == "cp" and old_file_name != new_file_name:
        with (open(old_file_name, "r") as old_file,
              open(new_file_name, "w") as new_file):
            new_file.write(old_file.read())
