def copy_file(command: str) -> None:
    split_command = command.split()
    first_check = len(split_command) == 3
    second_check = split_command[0] == "cp"
    third_check = split_command[1] != split_command[2]
    if first_check and second_check and third_check:
        with (
                open(split_command[1], "r") as in_file,
                open(split_command[2], "w") as out_file
        ):
            out_file.write(in_file.read())
