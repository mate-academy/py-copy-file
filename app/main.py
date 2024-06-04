def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "cp":
        return
    first_file, second_file = parts[1], parts[2]
    if first_file == second_file:
        return
    with (
        open(first_file, "r") as file_read,
        open(second_file, "w") as file_write
    ):
        file_write.write(file_read.read())
