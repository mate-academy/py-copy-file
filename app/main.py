def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "cp":
        print("Invalid command")
        return

    _, old_file, new_file = parts

    try:
        with open(old_file, "r") as file_in:
            if old_file != new_file:
                with open(new_file, "w") as file_out:
                    file_out.write(file_in.read())
    except FileNotFoundError:
        raise
