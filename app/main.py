def copy_file(command: str) -> None:
    operator, source_file, new_file = command.split()
    if source_file != new_file and operator == "cp":
        with (
            open(source_file, "r") as file_in,
            open(new_file, "w") as file_out
        ):
            file_out.write(file_in.read())
