def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "cp":
        return

    cp_command, file_name, copy_name = parts
    if file_name == copy_name:
        return

    try:
        with open(file_name, "r") as file_in, open(copy_name, "w") as file_out:
            for line in file_in:
                file_out.write(line)
    except FileNotFoundError:
        return
