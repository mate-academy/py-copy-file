def copy_file(command: str) -> None:
    try:
        command, existing_file_name, new_file_name = command.split(" ")
        if command != "cp" or existing_file_name == new_file_name:
            raise ValueError
    except ValueError:
        return

    try:
        with (
            open(existing_file_name, "r") as existing_file,
            open(new_file_name, "w") as new_file
        ):
            new_file.write(existing_file.read())
    except FileNotFoundError:
        return
