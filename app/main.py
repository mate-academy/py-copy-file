def copy_file(command: str) -> None:
    if command:
        split_command = command.split()
        file_name1 = split_command[1]
        file_name2 = split_command[2]

        if (
                len(split_command) == 3
                and split_command[0] == "cp"
                and file_name1 != file_name2
        ):

            with (
                open(file_name1, "r") as origin_file,
                open(file_name2, "w") as duplicate_file
            ):
                content_from_origin = origin_file.read()
                duplicate_file.write(content_from_origin)
