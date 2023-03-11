def copy_file(command: str) -> None:
    command, copied_file, file_to_copy = command.split()
    if copied_file != file_to_copy:
        with open(copied_file, "r") as file_in, \
                open(file_to_copy, "w") as file_out:
            file_out.write(file_in.read() + "\n")
