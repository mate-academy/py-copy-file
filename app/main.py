def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "cp":
        return

    file_name_to_copy = parts[1]
    future_file = parts[2]

    if file_name_to_copy == future_file:
        return

    try:
        with open(file_name_to_copy, "r") as original_file:
            content = original_file.read()
    except FileNotFoundError:
        return

    with open(future_file, "w") as new_file:
        new_file.write(content)
