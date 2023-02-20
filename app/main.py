def copy_file(command: str) -> None:
    short_command, name_f_in, name_f_out = command.split()

    if short_command == "cp" and name_f_in != name_f_out:
        with (
            open(name_f_in, "r") as file_in,
            open(name_f_out, "w") as file_out
        ):
            file_out.write(file_in.read())
