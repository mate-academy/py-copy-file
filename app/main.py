def copy_file(command: str) -> None:

    split_command = [word for word in command.split(" ")]
    command = split_command[0]
    file_name_in = split_command[1]
    file_name_out = split_command[2]

    if (
            len(split_command) == 3
            and command == "cp"
            and file_name_in != file_name_out
    ):

        with (
            open(file_name_in, "r") as file_in,
            open(file_name_out, "w") as file_out
        ):
            file_out.write(file_in.read())
