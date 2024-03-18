def copy_file(command: str) -> None:
    read_file = command.split()[1]
    write_file = command.split()[2]
    if read_file != write_file and command.split()[0] == "cp":
        with (
            open(read_file, "r") as file_in,
            open(write_file, "w") as file_out
        ):
            content = file_in.read()
            file_out.write(content)
