def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "cp":
        return

    first, second, third = parts

    if second == third:
        return

    try:
        with open(second, "r") as file_in, open(third, "w") as file_out:
            file_out.write(file_in.read())
    except FileNotFoundError:
        return
