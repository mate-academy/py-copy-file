def copy_file(command: str) -> None:
    new_file = command.split()

    if new_file == 3:
        if new_file[1] != new_file[2] and new_file[0] == "cp":
            with (
                open(command[1], "r") as file_in,
                open(command[2], "w") as file_out
            ):
                file_out.write(file_in.read())
