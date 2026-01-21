def copy_file(command: str) -> None:
    parts_of_command = command.split()

    if len(parts_of_command) != 3:
        print("Invalid value")
        return

    _, source_file, copied_file_name = parts_of_command

    if source_file == copied_file_name:
        print("Name of copied file should be new")
        return

    try:
        with (open(source_file, "r") as source,
              open(copied_file_name, "w") as copied_file):
            copied_file.write(source.read())
    except FileNotFoundError:
        print("Unfortunately file not found")
