def copy_file(command: str) -> None:
    command, original_file, new_file = command.split()

    if command != "cp":
        return

    if original_file == new_file:
        return

    with (
        open(original_file, "r") as file_in,
        open(new_file, "w") as file_out
    ):
        file_out.write(file_in.read())
