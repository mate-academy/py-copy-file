def copy_file(command: str) -> None:
    file_name = command.split()

    if file_name[0] == "cp":
        with open(
                file_name[1],
                "r"
        ) as file, open(
            file_name[2],
            "w"
        ) as file_copy:
            file_copy.write(file.read())
