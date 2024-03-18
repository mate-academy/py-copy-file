def copy_file(command: str) -> None:
    key, read_file, write_file, *_ = command.split()

    if read_file != write_file and key == "cp":
        with (
            open(read_file, "r") as file_in,
            open(write_file, "w") as file_out
        ):
            file_out.write(file_in.read())
