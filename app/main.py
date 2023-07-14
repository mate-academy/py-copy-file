def copy_file(command: str) -> None:
    command_split = command.split()
    if len(command_split) != 3:
        print("Invalid  usage. cp <file> <file_copy>")
        return
    command_name, filename, copy_filename = command_split
    if command_name != "cp":
        print("Invalid  usage. cp <file> <file_copy>")
        return
    if filename != copy_filename:
        with (
            open(filename, "r") as file,
            open(copy_filename, "w") as file_out
        ):
            file_out.write(file.read())
