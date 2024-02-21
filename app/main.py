def copy_file(command: str) -> None:
    element = command.split()

    if element[0] == "cp":
        with open(
                f"{element[1]}", "r"
        ) as file, open(
            f"{element[2]}", "a"
        ) as file_copy:

            if file.name != file_copy.name:
                file_copy.write(f"{file.read()}")
