def copy_file(command: str) -> None:

    if len(command) == 3:
        com, file_origin, file_copy = command.split()

        if com == "cp" and file_origin != file_copy:
            with (
                open(file_origin, "r") as file_in,
                open(file_copy, "w") as file_out
            ):
                file_out.write(file_in.read())
