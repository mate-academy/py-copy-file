def copy_file(command: str) -> None:
    act, first_file, second_file = command.split()
    if act == "cp" and first_file != second_file:
        with (open(first_file, "r") as file_in,
                open(second_file, "w") as file_out):
            file_out.write(file_in.read())
