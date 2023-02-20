def copy_file(command: str) -> None:
    command, old_file, new_file = command.split()

    if old_file != new_file and command == "cp":
        with open(
                old_file,
                "r"
        ) as file, open(
            new_file,
            "w"
        ) as file_copy:
            file_copy.write(file.read())
