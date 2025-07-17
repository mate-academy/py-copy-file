def copy_file(command: str) -> None:
    try:
        cmd, file_name, new_file_name = command.split(" ")
    except ValueError:
        return
    if file_name == new_file_name or cmd != "cp":
        return

    try:
        with open(file_name) as file, open(new_file_name, "w") as new_file:
            for line in file:
                new_file.write(line)
    except FileNotFoundError:
        return
