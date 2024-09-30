def copy_file(command: str) -> None:
    split_command = command.split()
    if (
            len(split_command) == 3
            and split_command[0] == "cp"
            and split_command[1] != split_command[2]
    ):
        with (
                open(split_command[1], "r") as in_file,
                open(split_command[2], "w") as out_file
        ):
            out_file.write(in_file.read())
