def copy_file(command: str) -> None:
    try:
        command, original_file, copy_of_file = command.split()
    except ValueError:
        return
    if command != "cp":
        return
    if original_file == copy_of_file:
        return
    with (
        open(original_file, "r") as file_in,
        open(copy_of_file, "w") as file_out,
    ):
        file_out.write(file_in.read())
