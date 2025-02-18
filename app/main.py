def copy_file(command: str) -> None:
    if not isinstance(command, str):
        raise TypeError("Command must be str type")
    command_split = command.split()
    if len(command_split) != 3 or command_split[0] != "cp":
        raise ValueError(
            "Command should be like this:"
            " cp file.txt file-copy.txt"
        )

    first_file_name = command_split[1]
    second_file_name = command_split[2]
    if first_file_name != second_file_name:
        with (
            open(first_file_name, "r") as first_file,
            open(second_file_name, "w") as second_file
        ):
            second_file.write(first_file.read())
