def copy_file(command: str) -> None:

    if len(command) == 3:
        com, orig_file, copyed_file = command.split()

        if com == "cp" and orig_file != copyed_file:
            with (
                open(orig_file, "r") as file_in,
                open(copyed_file, "w") as file_out
            ):
                file_out.write(file_in.read())
