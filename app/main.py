def copy_file(command: str) -> None:
    first_file = command.split(" ")[1]
    second_file = command.split(" ")[2]
    if first_file != second_file:
        with (
            open(first_file, "r") as file_in,
            open(second_file, "w") as file_out
        ):
            file_out.write(file_in.read())
