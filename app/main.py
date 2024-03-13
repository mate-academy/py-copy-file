def copy_file(command: str) -> None:
    file = command.split()

    if file == 3:
        if file[1] != file[2] and file[0] == "cp":
            with (
                open(command[1], "r") as file_in,
                open(command[2], "w") as file_out
            ):
                file_out.write(file_in.read())
