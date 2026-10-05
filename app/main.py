def copy_file(command: str) -> None:
    parts = command.split(" ")
    if len(parts) != 3 or parts[0] != "cp":
        return

    cp_command, old_name, new_name = parts
    if old_name == new_name:
        return

    try:
        with open(old_name, "r") as file_in, open(new_name, "w") as file_out:
            file_out.write(file_in.read())
    except FileNotFoundError:
        return
