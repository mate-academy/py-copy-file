def copy_file(command: str) -> None:
    command_sep = command.split()
    if len(command_sep) != 3:
        raise ValueError("Missed some arguments.")
    cp, file_in, file_out = command_sep
    if cp != "cp":
        raise ValueError("Incorrect command.")
    if file_in != file_out:
        with open(file_in, "r") as f_in, open(file_out, "w") as f_out:
            f_out.write(f_in.read())
