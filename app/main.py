def copy_file(command: str) -> None:
    parts = command.split()
    old_file = parts[1]
    new_file = parts[2]
    try:
        with open(old_file, "r") as file_in:
            if old_file != new_file:
                with open(new_file, "w") as file_out:
                    file_out.write(file_in.read())
    except FileNotFoundError:
        raise
