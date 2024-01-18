def copy_file(command: str) -> None:
    if len(command) > 3:
        file_names = command[3:].split()
        if (
                command[0:2] == "cp"
                and command.count(" ") == 2
                and file_names[0] != file_names[1]
        ):
            with (
                open(file_names[0], "r") as file_in,
                open(file_names[1], "w") as file_out
            ):
                file_out.write(file_in.read())
