def copy_file(command: str) -> None:
    _, copied_file_name, new_file_name = command.split()

    if copied_file_name != new_file_name:
        with (open(copied_file_name, "r") as copied_file,
              open(new_file_name, "w") as new_file):
            new_file.write(copied_file.read())
