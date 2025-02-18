def copy_file(command: str) -> None:
    split_command = command.split()

    if len(split_command) != 3:
        raise ValueError(
            "The command must contain three elements:"
            " 'cp', source file, and destination file."
        )

    if split_command[0] != "cp":
        raise ValueError(
            "The command must start with 'cp'."
        )

    if split_command[1] == split_command[2]:
        raise ValueError(
            "Source and destination file names are the same."
            " Copying to the same file is not allowed."
        )

    with open(split_command[1], "r") as file_in, \
            open(split_command[2], "w") as file_out:
        file_out.write(file_in.read())
