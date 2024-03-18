def copy_file(command: str) -> None:
    command = command.split()
    if len(command) == 3:
        key, f_in, f_out = command
        if key == "cp" and f_in != f_out:
            with (
                open(command[1], "r") as file_in,
                open(command[2], "w") as file_out
            ):
                file_out.write(file_in.read())
