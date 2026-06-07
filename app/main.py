def copy_file(command: str) -> None:
    command_parts = command.split()

    if len(command_parts) != 3:
        return

    command_name, file_to_copy, new_filename = command_parts

    if command_name != "cp":
        return
    if file_to_copy == new_filename:
        return
    try:
        with (open(file_to_copy, "r") as file,
              open(new_filename, "w") as new_file):
            new_file.write(file.read())
    except FileNotFoundError:
        print(f"File {file_to_copy} not found")
