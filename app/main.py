def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3:
        return
    comm, first_file, second_file = parts
    if comm != "cp":
        return
    if first_file == second_file:
        return
    try:
        with open(first_file) as file_1, open(second_file, "w") as file_copy:
            file_copy.write(file_1.read())
    except FileNotFoundError:
        return
