def copy_file(command: str) -> None:
    short_command, name_file_in, name_file_out = command.split()

    if short_command == "cp" and name_file_in != name_file_out:
        with (
            open(name_file_in, "r") as file_in,
            open(name_file_out, "w") as file_out
        ):
            file_out.write(file_in.read())
