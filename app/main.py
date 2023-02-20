def copy_file(command: str) -> None:
    command, to_copy, new = command.split()
    if to_copy != new and command == "cp":
        with (
            open(to_copy, "r") as file_to_copy,
            open(new, "w") as new_file
        ):
            new_file.write(file_to_copy.read())
