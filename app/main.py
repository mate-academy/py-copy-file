def copy_file(command: str) -> None:
    command, file, file_copy = command.split()
    if command == "cp" and file != file_copy:
        with (open(file, "r") as file_in, open(file_copy, "w") as file_out):
            file_out.write(file_in.read())
