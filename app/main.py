def copy_file(command_string: str) -> None:
    command, filename_in, filename_out, *_ = command_string.split()

    if command == "cp" and filename_in != filename_out:
        with (
            open(filename_in, "r") as file_in,
            open(filename_out, "w") as file_out
        ):
            file_out.write(file_in.read())
