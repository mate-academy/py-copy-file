def copy_file(command: str) -> None:
    if len(command.split()) == 3:
        cmd, filename, new_filename = command.split()
        if cmd == "cp" or filename != new_filename:
            with (
                open(filename, "r") as file_in,
                open(new_filename, "w") as file_out
            ):
                file_out.write(file_in.read())
