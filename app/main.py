def copy_file(command: str) -> None:
    command = command.split()
    if len(command) == 3:
        key, f_in, f_out = command
        if key == "cp" and f_in != f_out:
            with (
                open(f_in, "r") as file_in,
                open(f_out, "w") as file_out
            ):
                file_out.write(file_in.read())
